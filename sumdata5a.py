from itertools import islice
from PIL import Image



total=0
numscount=0
linec=0
date=""
for year in range(1980,2019):
	total=0
	for month in range(1,13):

		date=str(year)+"%02d" % (month,)

		with open('D:\\projects\\nasa\\mera_coem\\'+date+'.txt', 'r') as inp:
				img = Image.new( 'RGB', (577,360), "black") # Create a new black image
				pixels = img.load() # Create the pixel map
				y=0
				for line in islice(inp, 1, None):
					y=y+1
					x=0
					nums=line.split(",")
					lat=nums[0]
					nums = nums[:0] + nums[1 :]
					for num in nums:
						x=x+1
						numa = float(num)

						numscount+=1
						if (numa>1.43603e-10 and 371-y>38 and 371-y < 94  and x>287 and x <405):
							pixels[x,371-y] = (int(numa*50000000000), 0, 0)
							total += numa
	img.save('bmp\\'+date+'.bmp')
	print str(year)+" "+ str(total)