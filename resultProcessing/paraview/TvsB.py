# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
solidstl = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
solidstlDisplay = Show(solidstl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
solidstlDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# find source
model_128pvd = FindSource('model_128.pvd')

# show data in view
model_128pvdDisplay = Show(model_128pvd, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
model_128pvdDisplay.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(model_128pvd)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=model_128pvd)

# Properties modified on calculator1
calculator1.ResultArrayName = 'velocity'
calculator1.Function = 'ux*iHat+uy*jHat+uz*kHat'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'

# hide data in view
Hide(model_128pvd, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a query selection
QuerySelect(QueryString='(volume_factor == 0)', FieldType='POINT', InsideOut=1)

# set active source
SetActiveSource(calculator1)

# create a new 'Extract Selection'
extractSelection1 = ExtractSelection(registrationName='ExtractSelection1', Input=calculator1)

# show data in view
extractSelection1Display = Show(extractSelection1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractSelection1Display.Representation = 'Surface'

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(solidstl)

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=solidstl)

# Properties modified on transform1.Transform
transform1.Transform.Scale = [0.001, 0.001, 0.001]

# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'

# hide data in view
Hide(solidstl, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(extractSelection1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=transform1.Transform)

# create a new 'Point Dataset Interpolator'
pointDatasetInterpolator1 = PointDatasetInterpolator(registrationName='PointDatasetInterpolator1', Input=extractSelection1,
    Source=transform1)

# Properties modified on pointDatasetInterpolator1
pointDatasetInterpolator1.Kernel = 'GaussianKernel'

# Properties modified on pointDatasetInterpolator1.Kernel
pointDatasetInterpolator1.Kernel.Radius = 0.001

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
pointDatasetInterpolator1Display = Show(pointDatasetInterpolator1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
pointDatasetInterpolator1Display.Representation = 'Surface'

# hide data in view
Hide(extractSelection1, renderView1)

# hide data in view
Hide(transform1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=pointDatasetInterpolator1)

# Properties modified on calculator2
calculator2.ResultArrayName = 'PointZ'
calculator2.Function = 'coordsZ'

# show data in view
calculator2Display = Show(calculator2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'

# hide data in view
Hide(pointDatasetInterpolator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'PointZ'
pointZLUT = GetColorTransferFunction('PointZ')

# get opacity transfer function/opacity map for 'PointZ'
pointZPWF = GetOpacityTransferFunction('PointZ')

# create a query selection
QuerySelect(QueryString='(PointZ  == max(PointZ))', FieldType='POINT', InsideOut=0)

# create a new 'Extract Selection'
extractSelection2 = ExtractSelection(registrationName='ExtractSelection2', Input=calculator2)

# Get index information for maximum coordZ point
pointD = paraview.servermanager.Fetch(extractSelection2)
xValue = pointD.GetPoint(0)[0]
yValue = pointD.GetPoint(0)[1]
maxZ = pointD.GetPoint(0)[2]
zValue10top= maxZ*9/10
zValue10bottom= maxZ*1/10
zValue3top = maxZ*2/3
zValue3bottom = maxZ*1/3

# set active source
SetActiveSource(calculator2)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=calculator2)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [xValue, yValue, 0.0001]
clip1.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# show data in view
extractSelection2Display = Show(extractSelection2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractSelection2Display.Representation = 'Surface'

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
extractSelection2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(registrationName='top10I', Input=clip1)

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [xValue, yValue, zValue10top]
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

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
SetActiveSource(clip2)

# create a new 'Clip'
clip3 = Clip(registrationName='middle10', Input=clip2)

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [xValue, yValue, zValue10bottom]
clip3.ClipType.Normal = [0.0, 0.0, -1.0]

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
clip4 = Clip(registrationName='bottom10', Input=clip1)

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [xValue, yValue, zValue10bottom]
clip4.ClipType.Normal = [0.0, 0.0, 1.0]

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

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip4.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# create a new 'Clip'
clip5 = Clip(registrationName='top3', Input=clip1)

# Properties modified on clip5.ClipType
clip5.ClipType.Origin = [xValue, yValue, zValue3top]
clip5.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip5Display = Show(clip5, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip5Display.Representation = 'Surface'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip5.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# create a new 'Clip'
clip6 = Clip(registrationName='top3I', Input=clip1)

# Properties modified on clip6.ClipType
clip6.ClipType.Origin = [xValue, yValue, zValue3top]
clip6.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip6Display = Show(clip6, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip6Display.Representation = 'Surface'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip6Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip6)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip6.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# create a new 'Clip'
clip7 = Clip(registrationName='middle3', Input=clip6)

# Properties modified on clip7.ClipType
clip7.ClipType.Origin = [xValue, yValue, zValue3bottom]
clip7.ClipType.Normal = [0.0, 0.0, -1.0]

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

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip7.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# create a new 'Clip'
clip8 = Clip(registrationName='bottom3', Input=clip1)

# Properties modified on clip8.ClipType
clip8.ClipType.Origin = [xValue, yValue, zValue3bottom]
clip8.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip8Display = Show(clip8, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip8Display.Representation = 'Surface'

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
clip8Display.SetScalarBarVisibility(renderView1, True)

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
clip5Display_1 = Show(clip8, spreadSheetView1, 'SpreadSheetRepresentation')

# assign view to a particular cell in the layout
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=2)

# show data in view
clip3Display_1 = Show(clip3, spreadSheetView1, 'SpreadSheetRepresentation')

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'vtkOriginalPointIds', 'Points', 'Points_Magnitude', 'coefficient', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'shear_rate', 'shear_stress', 'ux', 'uy', 'uz', 'velocity', 'volume_factor', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'vtkOriginalPointIds', 'Points', 'Points_Magnitude', 'coefficient', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'shear_stress', 'ux', 'uy', 'uz', 'velocity', 'volume_factor', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'vtkOriginalPointIds', 'Points', 'Points_Magnitude', 'coefficient', 'fx', 'fy', 'fz', 'intensity', 'permeability', 'pressure', 'rt', 'ux', 'uy', 'uz', 'velocity', 'volume_factor', 'Block Number']

# export view
ExportView('/Users/yhao/Downloads/middle10.csv', view=spreadSheetView1)

# show data in view
clip4Display_1 = Show(clip4, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/bottom10.csv', view=spreadSheetView1)

# show data in view
clip5Display_1 = Show(clip5, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/top3.csv', view=spreadSheetView1)

# show data in view
clip7Display_1 = Show(clip7, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/middle3.csv', view=spreadSheetView1)

# show data in view
clip8Display_1 = Show(clip8, spreadSheetView1, 'SpreadSheetRepresentation')

# export view
ExportView('/Users/yhao/Downloads/bottom3.csv', view=spreadSheetView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1449, 1094)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.16380422772901648, 0.03608805313706398, 0.003643254263326526]
renderView1.CameraFocalPoint = [0.08370302990078926, 0.03608805313706398, 0.003643254263326526]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.020731715533469877

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).