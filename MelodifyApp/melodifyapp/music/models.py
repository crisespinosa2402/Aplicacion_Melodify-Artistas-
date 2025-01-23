from django.core.files.storage import default_storage
from io import BytesIO
from pydub import AudioSegment
from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    duration = models.DurationField(blank=True, null=True)
    file = models.FileField(upload_to='songs/')

    def save(self, *args, **kwargs):
        if self.file:
            try:
                # Abrir el archivo cargado por Django
                file_path = default_storage.path(self.file.name)  # Obtener la ruta completa del archivo
                audio = AudioSegment.from_file(file_path)  # Usar la ruta para abrir el archivo con Pydub

                # Guardar la duración del archivo de audio
                self.duration = audio.duration_seconds  # Duración en segundos
            except Exception as e:
                print(f"Error procesando el archivo con Pydub: {e}")
                self.duration = None
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.artist}"
