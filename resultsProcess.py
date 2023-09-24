# trace generated using paraview version 5.9.0
# This is a script to process the simulation results in paraview

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
solid_128_0000_000vtu = GetActiveSource()

# Properties modified on solid_128_0000_000vtu
solid_128_0000_000vtu.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solid_128_0000_000vtuDisplay = Show(solid_128_0000_000vtu, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
solid_128_0000_000vtuDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
solid_128_0000_000vtuDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Label'
labelLUT = GetColorTransferFunction('Label')

# get opacity transfer function/opacity map for 'Label'
labelPWF = GetOpacityTransferFunction('Label')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=solid_128_0000_000vtu)

# Properties modified on calculator1
calculator1.ResultArrayName = 'PointZ'
calculator1.Function = 'coordsZ'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'

# hide data in view
Hide(solid_128_0000_000vtu, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'PointZ'
pointZLUT = GetColorTransferFunction('PointZ')

# get opacity transfer function/opacity map for 'PointZ'
pointZPWF = GetOpacityTransferFunction('PointZ')

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)

# Properties modified on calculator2
calculator2.ResultArrayName = 'velocity'
calculator2.Function = 'ux*iHat+uy*jHat+uz*kHat'

# show data in view
calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a query selection
QuerySelect(QueryString='(PointZ  == max(PointZ))', FieldType='POINT', InsideOut=0)

# set active source
SetActiveSource(calculator2)

# create a new 'Extract Selection'
extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=calculator2)

# Get index information for maximum coordZ point
pointD = paraview.servermanager.Fetch(extractSelection1)
xValue = pointD.GetPoint(0)[0]
yValue = pointD.GetPoint(0)[1]
maxZ = pointD.GetPoint(0)[2]
Zvalue = maxZ*2/3

# show data in view
extractSelection1Display = Show(extractSelection1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractSelection1Display.Representation = 'Surface'

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
extractSelection1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(extractSelection1, renderView1)

# set active source
SetActiveSource(calculator2)

# show data in view
calculator2Display = Show(calculator2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=calculator2)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
extractSurface1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=extractSurface1)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [xValue, yValue, 0.0001]
clip1.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# hide data in view
Hide(extractSurface1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=clip1)

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [xValue, yValue, Zvalue]
clip2.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=clip1)

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [xValue, yValue, Zvalue]
clip3.ClipType.Normal = [0.0, -1.0, 0.0]

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip3.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# create a new 'Clip'
clip4 = Clip(registrationName='Clip4', Input=clip1)

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [xValue, yValue, Zvalue]
clip4.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip4Display = Show(clip4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip4Display.Representation = 'Surface'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
clip4Display_1 = Show(clip4, spreadSheetView1, 'SpreadSheetRepresentation')

# assign view to a particular cell in the layout
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=2)

# show data in view
calculator2Display_1 = Show(calculator2, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = []

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'PointZ', 'Points', 'Points_Magnitude', 'coefficient', 'elongation_rate', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'shear_rate', 'shear_stress', 'ux', 'uy', 'uz', 'velocity', 'velocity_Magnitude', 'volume_factor', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'PointZ', 'Points', 'Points_Magnitude', 'coefficient', 'elongation_rate', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'shear_rate', 'shear_stress', 'ux', 'uy', 'uz', 'velocity', 'volume_factor', 'Block Number']

# export view
ExportView('/Users/yhao/Downloads/volume.csv', view=spreadSheetView1)

# show data in view
clip1Display_1 = Show(clip1, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'PointZ', 'Points', 'Points_Magnitude', 'coefficient', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'shear_rate', 'shear_stress', 'ux', 'uy', 'uz', 'velocity', 'volume_factor', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'PointZ', 'Points', 'Points_Magnitude', 'coefficient', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'shear_stress', 'ux', 'uy', 'uz', 'velocity', 'volume_factor', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'PointZ', 'Points', 'Points_Magnitude', 'coefficient', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'ux', 'uy', 'uz', 'velocity', 'volume_factor', 'Block Number']

# export view
ExportView('/Users/yhao/Downloads/surface.csv', view=spreadSheetView1)

# show data in view
clip2Display_1 = Show(clip2, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/top.csv', view=spreadSheetView1)

# show data in view
clip3Display_1 = Show(clip3, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/faceward.csv', view=spreadSheetView1)

# show data in view
clip4Display_1 = Show(clip4, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/backward.csv', view=spreadSheetView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1453, 1094)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.08366339653730392, 0.036315194331109524, 0.08017969658442585]
renderView1.CameraFocalPoint = [0.08366339653730392, 0.036315194331109524, 0.0032228081472567283]
renderView1.CameraParallelScale = 0.019917908379369333

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).