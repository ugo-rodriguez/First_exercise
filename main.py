###Libraries
import argparse
import itk
import vtk
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkImagingCore import vtkImageCast
from vtkmodules.vtkImagingMath import vtkImageWeightedSum
from vtkmodules.vtkImagingSources import (
    vtkImageMandelbrotSource,
    vtkImageSinusoidSource
)
from vtkmodules.vtkRenderingCore import (
    vtkImageActor,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)



###main
def main():
    #Initialization argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("name_input",help="it's the name of the input image")
    parser.add_argument("name_output",help="it's the name of the output image")
    parser.add_argument("r", type = int,help="it's the radius for the filter")
    args = parser.parse_args()

    #Filename
    input_filename = args.name_input
    output_filename = args.name_output

    #Reading of input image
    pixel_type = itk.ctype("unsigned char")
    image = itk.imread(input_filename,pixel_type)

    #Application of median filter
    median = itk.median_image_filter(image, radius=args.r)
    itk.imwrite(median, output_filename)

    #Conversion of images in vtk type
    vtk_image = itk.vtk_image_from_image(image)
    vtk_median = itk.vtk_image_from_image(median)

    # Create an image actor
    image_actor = vtk.vtkImageActor()
    image_actor.SetInputData(vtk_image)
    
    median_actor = vtk.vtkImageActor()
    median_actor.SetInputData(vtk_median)
    
    # Create a renderer
    image_rend = vtk.vtkRenderer()
    image_rend.AddActor(image_actor)
    image_rend.SetViewport(0.0, 0.0, 0.5, 1.0)

    median_rend = vtk.vtkRenderer()
    median_rend.AddActor(median_actor)
    median_rend.SetViewport(0.5, 0.0, 1.0, 1.0)

    #Create a Window
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(image_rend)
    renWin.AddRenderer(median_rend)
    renWin.SetSize(600, 300)
    renWin.SetWindowName("Original and filtered (median) image")



    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(renWin)
    render_window_interactor.Start()


if __name__ == '__main__':
  main()