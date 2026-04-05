import cv2
import numpy as np
import os


def cv2_imread_chinese(path):

    try:
        if not os.path.exists(path):
            print(f"Error: The file does not exist → {path}")
            return None

        stream = open(path.encode('utf-8'), 'rb')
        bytes_data = bytearray(stream.read())
        np_data = np.asarray(bytes_data, dtype=np.uint8)
        img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
        stream.close()
        return img
    except Exception as e:
        print(f"Failed to read the file → {path}，Error：{str(e)}")
        return None


def cv2_imwrite_chinese(path, img):

    try:
        
        output_dir = os.path.dirname(path)
        os.makedirs(output_dir, exist_ok=True)

        ext = os.path.splitext(path)[-1]
        result, encoded_img = cv2.imencode(ext, img)
        if result:
            encoded_img.tofile(path.encode('utf-8'))
            return True
        else:
            return False
    except Exception as e:
        print(f"Failed to save the file → {path}，错误：{str(e)}")
        return False


def add_fog_to_image(clean_image_path, mask_path, output_path, fog_color=(255, 255, 255), intensity=1):


    img = cv2_imread_chinese(clean_image_path)
    mask = cv2_imread_chinese(mask_path)

    if img is None:
        print(f"\n❌ Failed to read the original image：{clean_image_path}")
        return
    if mask is None:
        print(f"\n❌ Mask reading failed：{mask_path}")
        return

    if len(mask.shape) == 3:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    h, w, _ = img.shape
    mask_resized = cv2.resize(mask, (w, h))

    img_float = img.astype(float) / 255.0
    mask_float = mask_resized.astype(float) / 255.0
    mask_float = np.clip(mask_float * intensity, 0, 1.0)
    alpha = mask_float[:, :, np.newaxis]

    fog_color_norm = np.array(fog_color).astype(float) / 255.0
    atmospheric_light = np.full_like(img_float, fog_color_norm)
    blended = img_float * (1 - alpha) + atmospheric_light * alpha

    result = (blended * 255).astype(np.uint8)

    save_success = cv2_imwrite_chinese(output_path, result)

    if save_success and os.path.exists(output_path):
        file_size = os.path.getsize(output_path) / 1024  # KB
        print(f"\n✅ Saved successfully！")
        print(f"📁 Save path：{output_path}")
        print(f"📏 File size：{file_size:.2f} KB")
    else:

        fallback_path = r'C:\Users\Admin\Desktop\fog_result_13.jpg'
        cv2.imwrite(fallback_path, result)
        print(f"\n⚠️ The original path save failed. It has been saved as a fallback option to：{fallback_path}")


if __name__ == "__main__":

    CLEAN_IMG = r'C:\Users\Admin\Desktop6962.jpg'
    FOG_MASK = r'C:\Users\Admin\Desktop55.png'
    RESULT_IMG = r'C:\Users\Admin\Desktop\6962-1.jpg'

    add_fog_to_image(
        clean_image_path=CLEAN_IMG,
        mask_path=FOG_MASK,
        output_path=RESULT_IMG,
        fog_color=(240, 200, 220),
        intensity=1.6
    )