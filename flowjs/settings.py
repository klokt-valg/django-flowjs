from django.conf import settings

# Media path where the files are saved
# Files will be saved to default file storage
FLOWJS_PATH = getattr(settings, "FLOWJS_PATH", 'flowjs/')

# Indicates whether to use local storage or default storage
FLOWJS_USE_LOCALSTORAGE = getattr(settings, "FLOWJS_USE_LOCALSTORAGE", False)

# Remove the upload files when the model is deleted
FLOWJS_REMOVE_FILES_ON_DELETE = getattr(settings, "FLOWJS_REMOVE_FILES_ON_DELETE", True)

# Remove temporary chunks after file have been upload and created
FLOWJS_AUTO_DELETE_CHUNKS = getattr(settings, "FLOWJS_AUTO_DELETE_CHUNKS", True)

# Time in days to remove non completed uploads
FLOWJS_EXPIRATION_DAYS = getattr(settings, "FLOWJS_EXPIRATION_DAYS", 1)

# When flowjs should join files in background. Options: 'none', 'media' (audio and video), 'all' (all files).
FLOWJS_JOIN_CHUNKS_IN_BACKGROUND = getattr(settings, "FLOWJS_JOIN_CHUNKS_IN_BACKGROUND", 'none')

# Check if FLOWJS should use Celery
FLOWJS_WITH_CELERY = getattr(settings, "FLOWJS_USE_CELERY", False)
