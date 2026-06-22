from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from filesystem_api.models import Directory, File
from filesystem_api.services.filesystem_service import FileSystemService
from filesystem_api.services.search_service import SearchService


# =========================
# SEARCH API
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request):

    query = request.GET.get("q")

    if not query:
        return Response({"error": "Search query required"}, status=400)

    result = SearchService.global_search(query, request.user)

    files = result.get("files", [])
    directories = result.get("directories", [])

    return Response({
        "query": query,
        "files": [
            {"id": f.id, "name": f.name} for f in files
        ],
        "directories": [
            {"id": d.id, "name": d.name} for d in directories
        ]
    })


# =========================
# CREATE DIRECTORY (mkdir)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_directory(request):

    name = request.data.get("name")
    parent_id = request.data.get("parent_id")

    if not name:
        return Response({"error": "Directory name required"}, status=400)

    parent = None
    if parent_id:
        try:
            parent = Directory.objects.get(
                id=parent_id,
                owner=request.user
            )
        except Directory.DoesNotExist:
            return Response(
                {"error": "Parent directory not found"},
                status=404
            )

    directory = FileSystemService.create_directory(
        name=name,
        owner=request.user,
        parent=parent
    )

    return Response({
        "message": "Directory created successfully",
        "id": directory.id,
        "name": directory.name,
        "parent": parent.id if parent else None
    })


# =========================
# CREATE FILE (touch)
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_file(request):

    name = request.data.get("name")
    content = request.data.get("content", "")
    directory_id = request.data.get("directory_id")

    if not name or not directory_id:
        return Response({"error": "name and directory_id required"}, status=400)

    try:
        directory = Directory.objects.get(
            id=directory_id,
            owner=request.user
        )
    except Directory.DoesNotExist:
        return Response({"error": "Directory not found"}, status=404)

    file = FileSystemService.create_file(
        name=name,
        content=content,
        owner=request.user,
        directory=directory
    )

    return Response({
        "message": "File created successfully",
        "id": file.id,
        "name": file.name
    })


# =========================
# LIST DIRECTORY (ls)
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_directory(request, directory_id):

    try:

        data = FileSystemService.list_directory(
            directory_id,
            request.user
        )

        if not data:
            return Response(
                {"error": "Directory not found"},
                status=404
            )

        current_dir = Directory.objects.get(
            id=directory_id,
            owner=request.user
        )

        # =========================
        # BUILD BREADCRUMB
        # =========================
        breadcrumb = []

        temp = current_dir

        while temp:
            breadcrumb.insert(0, {
                "id": temp.id,
                "name": temp.name
            })

            temp = temp.parent

        return Response({

            "breadcrumb": breadcrumb,

            "current_directory": {
                "id": current_dir.id,
                "name": current_dir.name
            },

            "directories": [
                {
                    "id": d.id,
                    "name": d.name
                }
                for d in data["directories"]
            ],

            "files": [
                {
                    "id": f.id,
                    "name": f.name
                }
                for f in data["files"]
            ]
        })

    except Directory.DoesNotExist:
        return Response(
            {"error": "Directory not found"},
            status=404
        )

    except Exception as e:

        return Response({
            "error": "Internal server error",
            "details": str(e)
        }, status=500)
    
# =========================
# DELETE FILE
# =========================    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_file(request, file_id):

    success = FileSystemService.delete_file(
        file_id=file_id,
        owner=request.user
    )

    if not success:
        return Response(
            {"error": "File not found"},
            status=404
        )

    return Response({
        "message": "File moved to recycle bin"
    })

# =========================
# MOVE FILE
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def move_file(request):

    file_id = request.data.get("file_id")
    destination_folder_name = request.data.get(
        "destination_folder_name"
    )

    if not file_id or not destination_folder_name:
        return Response(
            {
                "error": "file_id and destination_folder_name required"
            },
            status=400
        )

    try:
        destination_directory = Directory.objects.get(
            name=destination_folder_name,
            owner=request.user
        )

    except Directory.DoesNotExist:
        return Response(
            {
                "error": "Destination folder not found"
            },
            status=404
        )

    success = FileSystemService.move_file(
        file_id=file_id,
        destination_directory_id=destination_directory.id,
        owner=request.user
    )

    if not success:
        return Response(
            {
                "error": "Move failed"
            },
            status=404
        )

    return Response(
        {
            "message": "File moved successfully"
        }
    )

# =========================
# MOVE DIRECTORY
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def move_directory(request):

    directory_id = request.data.get(
        "directory_id"
    )

    destination_folder_name = request.data.get(
        "destination_folder_name"
    )

    if not directory_id or not destination_folder_name:
        return Response(
            {
                "error": "directory_id and destination_folder_name required"
            },
            status=400
        )

    try:

        destination_directory = Directory.objects.get(
            name=destination_folder_name,
            owner=request.user
        )

    except Directory.DoesNotExist:

        return Response(
            {
                "error": "Destination folder not found"
            },
            status=404
        )

    success = FileSystemService.move_directory(
        directory_id=directory_id,
        destination_directory_id=destination_directory.id,
        owner=request.user
    )

    if not success:

        return Response(
            {
                "error": "Move failed"
            },
            status=404
        )

    return Response(
        {
            "message": "Directory moved successfully"
        }
    )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_directory(request, directory_id):

    success = FileSystemService.delete_directory(
        directory_id=directory_id,
        owner=request.user
    )

    if not success:
        return Response(
            {"error": "Directory not found"},
            status=404
        )

    return Response({
        "message": "Directory moved to recycle bin"
    })