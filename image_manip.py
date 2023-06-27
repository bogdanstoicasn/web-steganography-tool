from PIL import Image
import os
import sys

def encode_message(image_path, message, image_name):
	message = message + '*'
	img = Image.open(image_path)
	img = img.convert('RGB')

	width, height = img.size
	pixels = list(img.getdata())

	if len(message) > len(pixels) * 3:
		return "Message too long for this image!"

	encoded_pixels = []
	message_index = 0

	for pixel in pixels:
		r, g, b = pixel

		if message_index < len(message):
			ascii_val = ord(message[message_index])

			# Encode the message bits into the least significant bits of the pixel values
			r = (r & 0xF8) | ((ascii_val >> 5) & 0x07)
			g = (g & 0xF8) | ((ascii_val >> 2) & 0x07)
			b = (b & 0xFC) | ((ascii_val >> 0) & 0x03)

			encoded_pixels.append((r, g, b))
			message_index += 1
		else:
			encoded_pixels.append(pixel)

	encoded_img = Image.new(img.mode, img.size)
	encoded_img.putdata(encoded_pixels)
	encoded_img.save(image_name)

	return "Encoding completed successfully!"

def decode_message(image_path):
	img = Image.open(image_path)
	img = img.convert('RGB')

	pixels = list(img.getdata())

	message = ""
	message_index = 0

	while True:
		pixel = pixels[message_index]
		r, g, b = pixel

		# Decode the least significant bits of the pixel values into the message bits
		ascii_val = ((r & 0x07) << 5) | ((g & 0x07) << 2) | ((b & 0x03) << 0)

		if chr(ascii_val) in ['#', '*', '\n']:
			break

		message += chr(ascii_val)
		message_index += 1

	return message

def main():
	args = sys.argv[1:]

	if len(args) < 2:
		print("Invalid number of arguments.")
		print("Usage: python image_manip.py <command> <image_path> [<message> [<output_name>]]")
		return

	command = args[0]
	image_path = args[1]

	if not os.path.exists(image_path):
		print("Image path does not exist!")
		return

	if command == 'encode':
		if len(args) < 4:
			print("Invalid number of arguments for encoding.")
			print("Usage: python image_manip.py encode <image_path> <message> <output_name>")
			return

		message = args[2]
		output_name = args[3]
		result = encode_message(image_path, message, output_name)
		print(result)
	elif command == 'decode':
		result = decode_message(image_path)
		print("Decoded message: " + result)
	else:
		print("Invalid command.")
		print("Usage: python image_manip.py <command> <image_path> [<message> [<output_name>]]")
		return

if __name__ == '__main__':
	main()

