from SimpleCV import *
pattern_image = Image("cursor.png")
mask_image = Image("mask.png").grayscale()
cam = VirtualCamera("output.avi", 'video')
last_frame = None
img = None

def find_and_subtract_cursor(img):
	found_patterns = img.findTemplate(pattern_image, 200)
	x = found_patterns.x()[0]
	y = found_patterns.y()[0]
	# print found_patterns
	new_img = mask_image.copy().embiggen(img.size(), pos=(x, y + 1))
	return (x, y, new_img)



for i in range(50, 400):
	last_frame = img
	img = cam.getFrame(i)
	if last_frame is None:
		continue

	x, y, new_mask = find_and_subtract_cursor(img)
	old_x, old_y, old_mask = find_and_subtract_cursor(last_frame)

	sub = ((img.grayscale() - last_frame.grayscale()) - new_mask - old_mask).binarize(128)
	corners = sub.findCorners()
	if corners is not None:
		corners.draw()
	# blobs = sub.findBlobs()
	# if blobs is not None:
	# blobs.draw(autocolor=True)
	sub.show()

	# print found_patterns

	# found_patterns = last_frame.findTemplate(pattern_image, 200)
	# print found_patterns
	# print "--"


	# (img.grayscale() - last_frame.grayscale()).show()


	# found_patterns.show()
	# print i, found_patterns.x(), found_patterns.y()
	# found_patterns.draw()
	# img.show()
