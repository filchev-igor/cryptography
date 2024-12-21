from stegano import lsb

def hide_data(input_image_path, output_image_path, secret_message):
    """Hide a secret message inside an image."""
    secret_image = lsb.hide(input_image_path, secret_message)
    secret_image.save(output_image_path)

def reveal_data(image_path):
    """Extract the hidden message from an image."""
    return lsb.reveal(image_path)
