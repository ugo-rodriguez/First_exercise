###Libraries
import argparse
import itk



###main
parser = argparse.ArgumentParser()
parser.add_argument("name_input",help="it's the name of the input image")
parser.add_argument("name_output",help="it's the name of the output image")
args = parser.parse_args()

input_filename = args.name_input
output_filename = args.name_output

pixel_type = itk.ctype("unsigned char")
image = itk.imread(input_filename,pixel_type)

median = itk.median_image_filter(image, radius=10)
itk.imwrite(median, output_filename)
