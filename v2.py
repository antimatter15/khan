from SimpleCV import *
import numpy as np

pattern_image = Image("cursor.png")
mask_image = Image("mask.png").grayscale()
cam = VirtualCamera("output.avi", 'video')
last_frame = None
img = None
old_coords = (-1, -1)
# old_masked = None
last_complete = None


def find_and_subtract_cursor(img):
	found_patterns = img.findTemplate(pattern_image, 200)
	if len(found_patterns) is not 1:
		return (-1, -1, None)

	x = found_patterns.x()[0]
	y = found_patterns.y()[0]
	# print found_patterns
	new_img = mask_image.copy().embiggen(img.size(), pos=(x, y + 1))
	return (x, y, new_img)



for i in range(10, 10473):
	last_frame = img
	
	next_img = cam.getFrame(i)
	draw = DrawingLayer((next_img.width, next_img.height))
	
	x, y, new_mask = find_and_subtract_cursor(next_img)
	
	next_img = next_img.grayscale().binarize(60).invert()


	if x < 0 or y < 0:
		img = next_img
		continue

	# if old_masked is None:
	# 	old_masked = Image((next_img.width, next_img.height))
	
	if last_complete is None:
		last_complete = Image((next_img.width, next_img.height))

	img = next_img - new_mask
	
	# old_mask = old_masked
	# old_masked = new_mask

	(old_x, old_y) = old_coords
	old_coords = (x, y)

	if last_frame is None:
		continue

	draw.circle((x + 6, y + 1), 10, color=Color.RED)

	
	# old_x, old_y, old_mask = find_and_subtract_cursor(last_frame)

	# if old_x < 0 or old_y < 0:
	# 	continue
	
	sub = (img.copy() - last_complete).binarize(60)

	last_complete = last_complete + img.copy()

	
	# sub = ((img.copy() - last_frame.copy()) - old_mask).binarize(60)
	corners = sub.findCorners()
	if corners is not None:
		corners.draw()
	# blobs = sub.findBlobs()
	# if blobs is not None:
	# blobs.draw(autocolor=True)
	last_complete.addDrawingLayer(draw)
	last_complete.addDrawingLayer(sub.getDrawingLayer())
	last_complete.applyLayers()
	last_complete.show()
	# img.addDrawingLayer(draw)
	# img.applyLayers()
	# img.show()

	# print found_patterns

	# found_patterns = last_frame.findTemplate(pattern_image, 200)
	# print found_patterns
	# print "--"
	# print sub.getNumpy()
	# np.dstack(np.where(sub.getNumpy()[:,:,0] == 0))
	on_pix = np.transpose(np.where(sub.getNumpy()[:,:,0] == 0))
	print i, (x, y), [(corner.x, corner.y) for corner in corners], [(c[0], c[1]) for c in on_pix]

	# (img.grayscale() - last_frame.grayscale()).show()


	# found_patterns.show()
	# print i, found_patterns.x(), found_patterns.y()
	# found_patterns.draw()
	# img.show()

