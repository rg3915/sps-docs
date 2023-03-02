from django.urls import path

from .views import (
    import_file,
    validate,
    download_sample,
    generic_import_file,
    generic_validate,
    generic_download_sample,
)

app_name = "thematic_areas"
urlpatterns = [
    path("validate", view=validate, name="validate"),
    path("import", view=import_file, name="import_file"),
    path("download", view=download_sample, name="download_sample"),
    path("validate_generic", view=generic_validate, name="validate"),
    path("import_generic", view=generic_import_file, name="import_file"),
    path("download_generic", view=generic_download_sample, name="download_sample"),
]
