from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    upload = FileField('Image',validators=[FileRequired(), FileAllowed(['png', 'jpg','Images only!'])])