class MediaType:
    AUDIO = "audio"
    IMAGE = "image"
    ARCHIVE = "archive"
    PHOTO = "photograph"
    MAP = "map"
    TRAVEL = "travel"
    VIDEO  = "video"
    SHEET = "sheet"
    OTHER = "other"
    MANUSCRIPT = "manuscript"
    EBOOK = "ebook"

    choices = (
        (OTHER, "אחר"),
        (AUDIO, "שיר"),
        (IMAGE, "תמונה"),
        (ARCHIVE, "פריט ארכיון"),
        (PHOTO, "צילום"),
        (MAP, "מפה"),
        (TRAVEL, "יומן מסע"),
        (VIDEO, "קטע וידאו"),
        (SHEET, "גליון"),
        (MANUSCRIPT, "כתב יד"),
        (EBOOK, "ספר אלקטרוני"),
    )


    all = {x[0] for x in choices}
