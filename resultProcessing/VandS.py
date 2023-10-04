# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
extractSelection1 = FindSource('ExtractSelection1')

# create a new 'Clip'
clip6 = Clip(registrationName='Clip6', Input=extractSelection1)

# find source
solidstl = FindSource('solid.stl')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solidstlDisplay = Show(solidstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
solidstlDisplay.Representation = 'Surface'

# find source
model_128pvd = FindSource('model_128.pvd')

# show data in view
model_128pvdDisplay = Show(model_128pvd, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
model_128pvdDisplay.Representation = 'Surface'

# find source
calculator1 = FindSource('Calculator1')

# find source
transform1 = FindSource('Transform1')

# find source
pointDatasetInterpolator1 = FindSource('PointDatasetInterpolator1')

# find source
clip2 = FindSource('Clip2')

# find source
extractSelection2 = FindSource('ExtractSelection2')

# find source
clip5 = FindSource('Clip5')

# find source
clip4 = FindSource('Clip4')

# find source
clip3 = FindSource('Clip3')

# find source
clip1 = FindSource('Clip1')

# find source
calculator2 = FindSource('Calculator2')

# show data in view
clip6Display = Show(clip6, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip6Display.Representation = 'Surface'

# hide data in view
Hide(extractSelection1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(model_128pvd, renderView1)

# hide data in view
Hide(solidstl, renderView1)

# find view
spreadSheetView1 = FindViewOrCreate('SpreadSheetView1', viewtype='SpreadSheetView')

# set active view
SetActiveView(spreadSheetView1)

# show data in view
clip6Display_1 = Show(clip6, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/1volume.csv', view=spreadSheetView1)

# Properties modified on clip6.ClipType
clip6.ClipType.Normal = [-1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView('/Users/yhao/Downloads/2volume.csv', view=spreadSheetView1)

# set active view
SetActiveView(renderView1)

# hide data in view
Hide(clip6, renderView1)

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip6.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# get color transfer function/color map for 'PointZ'
pointZLUT = GetColorTransferFunction('PointZ')

# get opacity transfer function/opacity map for 'PointZ'
pointZPWF = GetOpacityTransferFunction('PointZ')

# create a new 'Clip'
clip7 = Clip(registrationName='Clip7', Input=clip1)

# show data in view
clip7Display = Show(clip7, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip7Display.Representation = 'Surface'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip7Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active view
SetActiveView(spreadSheetView1)

# show data in view
clip7Display_1 = Show(clip7, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/1surface.csv', view=spreadSheetView1)

# Properties modified on clip7.ClipType
clip7.ClipType.Normal = [-1.0, 0.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView('/Users/yhao/Downloads/2surface.csv', view=spreadSheetView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1449, 1094)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.048034120351076126, 0.04465469345450401, 0.26927827329409965]
renderView1.CameraFocalPoint = [0.048034120351076126, 0.04465469345450401, 9.99999999999994e-05]
renderView1.CameraParallelScale = 0.07101517849407048

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).