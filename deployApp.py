# Final Project

# Nadya Arda Angraini - 1301204153
# Denada Putrisia - 1301204197

import pandas as pd
import numpy as np
import random
import bokeh
from bokeh.layouts import layout,row, column,widgetbox,gridplot
from bokeh.plotting import figure, output_file,show
from bokeh.io import curdoc, show, output_notebook, output_file
from bokeh.models.tools import HoverTool
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Select, Slider, TextInput
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import ColorPicker
from bokeh.models import RangeTool

#read dataset
cvd = pd.read_csv('covid_19_indonesia_time_series_all.csv')

cvdIDAC = cvd[cvd['Location ISO Code'] == 'ID-AC']
cvdIDBA = cvd[cvd['Location ISO Code'] == 'ID-BA']
cvdIDBT = cvd[cvd['Location ISO Code'] == 'ID-BT']
cvdIDBE = cvd[cvd['Location ISO Code'] == 'ID-BE']
cvdIDJK =	cvd[cvd['Location ISO Code'] == 'ID-JK']
cvdIDYO	=	cvd[cvd['Location ISO Code'] == 'ID-YO']
cvdIDGO	=	cvd[cvd['Location ISO Code'] == 'ID-GO']
cvdIDN	=	cvd[cvd['Location ISO Code'] == 'IDN']
cvdIDJA	=	cvd[cvd['Location ISO Code'] == 'ID-JA']
cvdIDJB	=	cvd[cvd['Location ISO Code'] == 'ID-JB']
cvdIDJT	=	cvd[cvd['Location ISO Code'] == 'ID-JT']
cvdIDJI	=	cvd[cvd['Location ISO Code'] == 'ID-JI']
cvdIDKB	=	cvd[cvd['Location ISO Code'] == 'ID-KB']
cvdIDKS	=	cvd[cvd['Location ISO Code'] == 'ID-KS']
cvdIDKT	=	cvd[cvd['Location ISO Code'] == 'ID-KT']
cvdIDKI	=	cvd[cvd['Location ISO Code'] == 'ID-KI']
cvdIDKU	=	cvd[cvd['Location ISO Code'] == 'ID-KU']
cvdIDBB	=	cvd[cvd['Location ISO Code'] == 'ID-BB']
cvdIDKR	=	cvd[cvd['Location ISO Code'] == 'ID-KR']
cvdIDLA	=	cvd[cvd['Location ISO Code'] =='ID-LA']
cvdIDMA	=	cvd[cvd['Location ISO Code'] == 'ID-MA']
cvdIDMU	=	cvd[cvd['Location ISO Code'] == 'ID-MU']
cvdIDNB	=	cvd[cvd['Location ISO Code'] == 'ID-NB']
cvdIDNT	=	cvd[cvd['Location ISO Code'] == 'ID-NT']
cvdIDPA	=	cvd[cvd['Location ISO Code'] == 'ID-PA']
cvdIDPB	=	cvd[cvd['Location ISO Code'] == 'ID-PB']
cvdIDRI	=	cvd[cvd['Location ISO Code'] == 'ID-RI']
cvdIDSR	=	cvd[cvd['Location ISO Code'] == 'ID-SR']
cvdIDSN	=	cvd[cvd['Location ISO Code'] == 'ID-SN']
cvdIDST	=	cvd[cvd['Location ISO Code'] == 'ID-ST']
cvdIDSG	=	cvd[cvd['Location ISO Code'] == 'ID-SG']
cvdIDSA	=	cvd[cvd['Location ISO Code'] == 'ID-SA']
cvdIDSB	=	cvd[cvd['Location ISO Code'] == 'ID-SB']
cvdIDSS	=	cvd[cvd['Location ISO Code'] == 'ID-SS']
cvdIDSU	=	cvd[cvd['Location ISO Code'] == 'ID-SU']

cvdIDAC['Date'] = pd.to_datetime(cvdIDAC['Date'])
cvdIDBA['Date'] = pd.to_datetime(cvdIDBA['Date'])
cvdIDBT['Date'] = pd.to_datetime(cvdIDBT['Date'])
cvdIDBE['Date'] = pd.to_datetime(cvdIDBE['Date'])
cvdIDJK['Date'] =	pd.to_datetime(cvdIDJK['Date'])
cvdIDYO['Date']	=	pd.to_datetime(cvdIDYO['Date'])
cvdIDGO['Date']	=	pd.to_datetime(cvdIDGO['Date'])
cvdIDN['Date']	=	pd.to_datetime(cvdIDN['Date'])
cvdIDJA['Date']	=	pd.to_datetime(cvdIDJA['Date'])
cvdIDJB['Date']	=	pd.to_datetime(cvdIDJB['Date'])
cvdIDJT['Date']	=	pd.to_datetime(cvdIDJT['Date'])
cvdIDJI['Date']	=	pd.to_datetime(cvdIDJI['Date'])
cvdIDKB['Date']	=	pd.to_datetime(cvdIDKB['Date'])
cvdIDKS['Date']	=	pd.to_datetime(cvdIDKS['Date'])
cvdIDKT['Date']	=	pd.to_datetime(cvdIDKT['Date'])
cvdIDKI['Date']	=	pd.to_datetime(cvdIDKI['Date'])
cvdIDKU['Date']	=	pd.to_datetime(cvdIDKU['Date'])
cvdIDBB['Date']	=	pd.to_datetime(cvdIDBB['Date'])
cvdIDKR['Date']	=	pd.to_datetime(cvdIDKR['Date'])
cvdIDLA['Date']	=	pd.to_datetime(cvdIDLA['Date'])
cvdIDMA['Date']	=	pd.to_datetime(cvdIDMA['Date'])
cvdIDMU['Date']	=	pd.to_datetime(cvdIDMU['Date'])
cvdIDNB['Date']	=	pd.to_datetime(cvdIDNB['Date'])
cvdIDNT['Date']	=	pd.to_datetime(cvdIDNT['Date'])
cvdIDPA['Date']	=	pd.to_datetime(cvdIDPA['Date'])
cvdIDPB['Date']	=	pd.to_datetime(cvdIDPB['Date'])
cvdIDRI['Date']	=	pd.to_datetime(cvdIDRI['Date'])
cvdIDSR['Date']	=	pd.to_datetime(cvdIDSR['Date'])
cvdIDSN['Date']	=	pd.to_datetime(cvdIDSN['Date'])
cvdIDST['Date']	=	pd.to_datetime(cvdIDST['Date'])
cvdIDSG['Date']	=	pd.to_datetime(cvdIDSG['Date'])
cvdIDSA['Date']	=	pd.to_datetime(cvdIDSA['Date'])
cvdIDSB['Date']	=	pd.to_datetime(cvdIDSB['Date'])
cvdIDSS['Date']	=	pd.to_datetime(cvdIDSS['Date'])
cvdIDSU['Date']	=	pd.to_datetime(cvdIDSU['Date'])

data_source_aceh = ColumnDataSource(cvdIDAC)
data_source_bali = ColumnDataSource(cvdIDBA)
data_source_banten = ColumnDataSource(cvdIDBT)
data_source_bengkulu = ColumnDataSource(cvdIDBE)
data_source_dki = ColumnDataSource(cvdIDJK)
data_source_diy = ColumnDataSource(cvdIDYO)
data_source_gorontalo = ColumnDataSource(cvdIDGO)
data_source_indonesia = ColumnDataSource(cvdIDN)
data_source_jambi = ColumnDataSource(cvdIDJA)
data_source_jabar = ColumnDataSource(cvdIDJB)
data_source_jateng = ColumnDataSource(cvdIDJT)
data_source_jatim = ColumnDataSource(cvdIDJI)
data_source_kalbar = ColumnDataSource(cvdIDKB)
data_source_kalsel = ColumnDataSource(cvdIDKS)
data_source_kalteng = ColumnDataSource(cvdIDKT)
data_source_kaltim = ColumnDataSource(cvdIDKI)
data_source_kalut = ColumnDataSource(cvdIDKU)
data_source_kepbangkab = ColumnDataSource(cvdIDBB)
data_source_kepriau = ColumnDataSource(cvdIDKR)
data_source_lampung = ColumnDataSource(cvdIDLA)
data_source_maluku = ColumnDataSource(cvdIDMA)
data_source_malukut = ColumnDataSource(cvdIDMU)
data_source_ntb = ColumnDataSource(cvdIDNB)
data_source_ntt = ColumnDataSource(cvdIDNT)
data_source_papua = ColumnDataSource(cvdIDPA)
data_source_papbar = ColumnDataSource(cvdIDPB)
data_source_riau = ColumnDataSource(cvdIDRI)
data_source_sulbar = ColumnDataSource(cvdIDSR)
data_source_sulsel = ColumnDataSource(cvdIDSN)
data_source_sulteng = ColumnDataSource(cvdIDST)
data_source_sultengg = ColumnDataSource(cvdIDSG)
data_source_sulut = ColumnDataSource(cvdIDSA)
data_source_sumbar = ColumnDataSource(cvdIDSB)
data_source_sumsel = ColumnDataSource(cvdIDSS)
data_source_sumut = ColumnDataSource(cvdIDSU)

dates1 = np.array(cvdIDAC['Date'])
fig1 = figure(x_axis_type='datetime',
             plot_height=1100, plot_width=1200,
             title='Covid-19 (New Cases)',
             x_axis_label='Year', y_axis_label='New Cases',
             x_range =(dates1[100],dates1[200]))

#new case
cvdIDAC1 = fig1.line('Date', 'New Cases', legend_label='Aceh', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_aceh)
cvdIDBA1 = fig1.line('Date', 'New Cases', legend_label='Bali', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_bali)
cvdIDBT1 = fig1.line('Date', 'New Cases', legend_label='Banten', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_banten)
cvdIDBE1 = fig1.line('Date', 'New Cases', legend_label='Bengkulu', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_bengkulu)
cvdIDJK1 = fig1.line('Date', 'New Cases', legend_label='DKI Jakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_dki)
cvdIDYO1 = fig1.line('Date', 'New Cases', legend_label='Daerah Istimewa Yogyakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_diy)
cvdIDGO1 = fig1.line('Date', 'New Cases', legend_label='Gorontalo', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_gorontalo)
cvdIDN1 = fig1.line('Date', 'New Cases', legend_label='Indonesia', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_indonesia)
cvdIDJA1 = fig1.line('Date', 'New Cases', legend_label='Jambi', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jambi)
cvdIDJB1 = fig1.line('Date', 'New Cases', legend_label='Jawa Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jabar)
cvdIDJT1 = fig1.line('Date', 'New Cases', legend_label='Jawa Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jateng)
cvdIDJI1 = fig1.line('Date', 'New Cases', legend_label='Jawa Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jatim)
cvdIDKB1 = fig1.line('Date', 'New Cases', legend_label='Kalimantan Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalbar)
cvdIDKS1 = fig1.line('Date', 'New Cases', legend_label='Kalimantan Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalsel)
cvdIDKT1 = fig1.line('Date', 'New Cases', legend_label='Kalimantan Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalteng)
cvdIDKI1 = fig1.line('Date', 'New Cases', legend_label='Kalimantan Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kaltim)
cvdIDKU1 = fig1.line('Date', 'New Cases', legend_label='Kalimantan Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalut)
cvdIDBB1 = fig1.line('Date', 'New Cases', legend_label='Kepulauan Bangka Belitung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kepbangkab)
cvdIDKR1 = fig1.line('Date', 'New Cases', legend_label='Kepulauan Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kepriau)
cvdIDLA1 = fig1.line('Date', 'New Cases', legend_label='Lampung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_lampung)
cvdIDMA1 = fig1.line('Date', 'New Cases', legend_label='Maluku', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_maluku)
cvdIDMU1 = fig1.line('Date', 'New Cases', legend_label='Maluku Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_malukut)
cvdIDNB1 = fig1.line('Date', 'New Cases', legend_label='Nusa Tenggara Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_ntb)
cvdIDNT1 = fig1.line('Date', 'New Cases', legend_label='Nusa Tenggara Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_ntt)
cvdIDPA1 = fig1.line('Date', 'New Cases', legend_label='Papua', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_papua)
cvdIDPB1 = fig1.line('Date', 'New Cases', legend_label='Papua Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_papbar)
cvdIDRI1 = fig1.line('Date', 'New Cases', legend_label='Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_riau)
cvdIDSR1 = fig1.line('Date', 'New Cases', legend_label='Sulawesi Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulbar)
cvdIDSN1 = fig1.line('Date', 'New Cases', legend_label='Sulawesi Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulsel)
cvdIDST1 = fig1.line('Date', 'New Cases', legend_label='Sulawesi Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulteng)
cvdIDSG1 = fig1.line('Date', 'New Cases', legend_label='Sulawesi Tenggara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sultengg)
cvdIDSA1 = fig1.line('Date', 'New Cases', legend_label='Sulawesi Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulut)
cvdIDSB1 = fig1.line('Date', 'New Cases', legend_label='Sumatera Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sumbar)
cvdIDSS1 = fig1.line('Date', 'New Cases', legend_label='Sumatera Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sumsel)
cvdIDSU1 = fig1.line('Date', 'New Cases', legend_label='Sumatera Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sumut)

# interaktif color
pickercvdIDAC1 = ColorPicker(title='set color Aceh',default_size=100)
pickercvdIDAC1.js_link('color', cvdIDAC1.glyph, 'line_color')

pickercvdIDBA1 = ColorPicker(title='set color Bali',default_size=100)
pickercvdIDBA1.js_link('color', cvdIDBA1.glyph, 'line_color')

pickercvdIDBT1 = ColorPicker(title='set color Banten',default_size=100)
pickercvdIDBT1.js_link('color', cvdIDBT1.glyph, 'line_color')

pickercvdIDBE1 = ColorPicker(title='set color Bengkulu',default_size=100)
pickercvdIDBE1.js_link('color', cvdIDBE1.glyph, 'line_color')

pickercvdIDJK1 = ColorPicker(title='set color DKI Jakarta',default_size=100)
pickercvdIDJK1.js_link('color', cvdIDJK1.glyph, 'line_color')

pickercvdIDYO1 = ColorPicker(title='set color Daerah Istimewa Yogyakarta',default_size=100)
pickercvdIDYO1.js_link('color', cvdIDYO1.glyph, 'line_color')

pickercvdIDGO1 = ColorPicker(title='set color Gorontalo',default_size=100)
pickercvdIDGO1.js_link('color', cvdIDGO1.glyph, 'line_color')

pickercvdIDN1 = ColorPicker(title='set color Indonesia',default_size=100)
pickercvdIDN1.js_link('color', cvdIDN1.glyph, 'line_color')

pickercvdIDJA1 = ColorPicker(title='set color Jambi',default_size=100)
pickercvdIDJA1.js_link('color', cvdIDJA1.glyph, 'line_color')

pickercvdIDJB1 = ColorPicker(title='set color Jawa Barat',default_size=100)
pickercvdIDJB1.js_link('color', cvdIDJB1.glyph, 'line_color')

pickercvdIDJT1 = ColorPicker(title='set color Jawa Tengah',default_size=100)
pickercvdIDJT1.js_link('color', cvdIDJT1.glyph, 'line_color')

pickercvdIDJI1 = ColorPicker(title='set color Jawa Timur',default_size=100)
pickercvdIDJI1.js_link('color', cvdIDJI1.glyph, 'line_color')

pickercvdIDKB1 = ColorPicker(title='set color Kalimantan Barat',default_size=100)
pickercvdIDKB1.js_link('color', cvdIDKB1.glyph, 'line_color')

pickercvdIDKS1 = ColorPicker(title='set color Kalimantan Selatan',default_size=100)
pickercvdIDKS1.js_link('color', cvdIDKS1.glyph, 'line_color')

pickercvdIDKT1 = ColorPicker(title='set color Kalimantan Tengah',default_size=100)
pickercvdIDKT1.js_link('color', cvdIDKT1.glyph, 'line_color')

pickercvdIDKI1 = ColorPicker(title='set color Kalimantan Timur',default_size=100)
pickercvdIDKI1.js_link('color', cvdIDKI1.glyph, 'line_color')

pickercvdIDKU1 = ColorPicker(title='set color Kalimantan Utara',default_size=100)
pickercvdIDKU1.js_link('color', cvdIDKU1.glyph, 'line_color')

pickercvdIDBB1 = ColorPicker(title='set color Kepulauan Bangka Belitung',default_size=100)
pickercvdIDBB1.js_link('color', cvdIDBB1.glyph, 'line_color')

pickercvdIDKR1 = ColorPicker(title='set color Kepulauan Riau',default_size=100)
pickercvdIDKR1.js_link('color', cvdIDKR1.glyph, 'line_color')

pickercvdIDLA1 = ColorPicker(title='set color Lampung',default_size=100)
pickercvdIDLA1.js_link('color', cvdIDLA1.glyph, 'line_color')

pickercvdIDMA1 = ColorPicker(title='set color Maluku',default_size=100)
pickercvdIDMA1.js_link('color', cvdIDMA1.glyph, 'line_color')

pickercvdIDMU1 = ColorPicker(title='set color Maluku Utara',default_size=100)
pickercvdIDMU1.js_link('color', cvdIDMU1.glyph, 'line_color')

pickercvdIDNB1 = ColorPicker(title='set color Nusa Tenggara Barat',default_size=100)
pickercvdIDNB1.js_link('color', cvdIDNB1.glyph, 'line_color')

pickercvdIDNT1 = ColorPicker(title='set color Nusa Tenggara Timur',default_size=100)
pickercvdIDNT1.js_link('color', cvdIDNT1.glyph, 'line_color')

pickercvdIDPA1 = ColorPicker(title='set color Papua',default_size=100)
pickercvdIDPA1.js_link('color', cvdIDPA1.glyph, 'line_color')

pickercvdIDPB1 = ColorPicker(title='set color Papua Barat',default_size=100)
pickercvdIDPB1.js_link('color', cvdIDPB1.glyph, 'line_color')

pickercvdIDRI1 = ColorPicker(title='set color Riau',default_size=100)
pickercvdIDRI1.js_link('color', cvdIDRI1.glyph, 'line_color')

pickercvdIDSR1 = ColorPicker(title='set color Sulawesi Barat',default_size=100)
pickercvdIDSR1.js_link('color', cvdIDSR1.glyph, 'line_color')

pickercvdIDSN1 = ColorPicker(title='set color Sulawesi Selatan',default_size=100)
pickercvdIDSN1.js_link('color', cvdIDSN1.glyph, 'line_color')

pickercvdIDST1 = ColorPicker(title='set color Sulawesi Tengah',default_size=100)
pickercvdIDST1.js_link('color', cvdIDST1.glyph, 'line_color')

pickercvdIDSG1 = ColorPicker(title='set color Sulawesi Tenggara',default_size=100)
pickercvdIDSG1.js_link('color', cvdIDSG1.glyph, 'line_color')

pickercvdIDSA1 = ColorPicker(title='set color Sulawesi Utara',default_size=100)
pickercvdIDSA1.js_link('color', cvdIDSA1.glyph, 'line_color')

pickercvdIDSB1 = ColorPicker(title='set color Sumatera Barat',default_size=100)
pickercvdIDSB1.js_link('color', cvdIDSB1.glyph, 'line_color')

pickercvdIDSS1 = ColorPicker(title='set color Sumatera Selatan',default_size=100)
pickercvdIDSS1.js_link('color', cvdIDSS1.glyph, 'line_color')

pickercvdIDSU1 = ColorPicker(title='set color Sumatera Utara',default_size=100)
pickercvdIDSU1.js_link('color', cvdIDSU1.glyph, 'line_color')

tooltips = [('Date','@Date{%F}'), ('Value', '@{New Cases}')]
formatters = {'@Date':'datetime'}

curdoc().theme = 'dark_minimal'

fig1.add_tools(HoverTool(renderers=[cvdIDAC1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDBA1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDBT1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDBE1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDJK1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDYO1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDGO1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDN1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDJA1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDJB1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDJT1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDJI1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDKB1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDKS1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDKT1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDKI1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDKU1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDBB1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDKR1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDLA1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDMA1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDMU1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDNB1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDNT1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDPA1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDPB1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDRI1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDSR1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDSN1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDST1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDSG1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDSA1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDSB1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDSS1],tooltips=tooltips,formatters=formatters))
fig1.add_tools(HoverTool(renderers=[cvdIDSU1],tooltips=tooltips,formatters=formatters))
fig1.legend.location = 'top_right'
fig1.legend.click_policy='hide'

layout1 = row(fig1,widgetbox(pickercvdIDAC1,pickercvdIDBA1,pickercvdIDBT1,pickercvdIDBE1,pickercvdIDJK1,pickercvdIDYO1,pickercvdIDGO1,pickercvdIDN1,pickercvdIDJA1,pickercvdIDJB1,pickercvdIDJT1,pickercvdIDJI1,pickercvdIDKB1,
                             pickercvdIDKS1,pickercvdIDKT1,pickercvdIDKI1,pickercvdIDKU1,pickercvdIDBB1,pickercvdIDKR1,pickercvdIDLA1,pickercvdIDMA1,pickercvdIDMU1,pickercvdIDNB1,pickercvdIDNT1,pickercvdIDPA1,pickercvdIDPB1,
                             pickercvdIDRI1,pickercvdIDSR1,pickercvdIDSN1,pickercvdIDST1,pickercvdIDSG1,pickercvdIDSA1,pickercvdIDSB1,pickercvdIDSS1,pickercvdIDSU1))
curdoc().add_root(layout1)

select1 = figure(title='Covid-19 (New Cases)',
        plot_height = 150,
        plot_width=1100,
        y_range=fig1.y_range,
        x_axis_type='datetime',
        tools='',
        x_axis_label='Year',
        y_axis_label='New Cases',
        toolbar_location =None)
range_tool = RangeTool(x_range=fig1.x_range)
range_tool.overlay.fill_color ='red'
range_tool.overlay.fill_alpha = .2

select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_aceh)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bali)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_banten)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bengkulu)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_dki)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_diy)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_gorontalo)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_indonesia)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jambi)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jabar)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jateng)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jatim)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalbar)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalsel)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalteng)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kaltim)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalut)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepbangkab)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepriau)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_lampung)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_maluku)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_malukut)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntb)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntt)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papua)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papbar)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_riau)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulbar)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulsel)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulteng)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sultengg)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulut)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumbar)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumsel)
select1.line('Date','New Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumut)


# select1.ygrid.gird_line_color=None
select1.add_tools(range_tool)
select1.toolbar.active_multi=range_tool

layoutsatu = column(select1)
# show(layoutsatu)

grid1 = gridplot([[layout1], [layoutsatu]])

# New Deaths
dates2 = np.array(cvdIDAC['Date'])
fig2 = figure(x_axis_type='datetime',
             plot_height=1100, plot_width=1100,
             title='Covid-19 (New Deaths)',
             x_axis_label='Year', y_axis_label='New Deaths',
             x_range =(dates2[100],dates2[200]))

cvdIDAC2 = fig2.line('Date', 'New Deaths', legend_label='Aceh', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_aceh)
cvdIDBA2 = fig2.line('Date', 'New Deaths', legend_label='Bali', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_bali)
cvdIDBT2 = fig2.line('Date', 'New Deaths', legend_label='Banten', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_banten)
cvdIDBE2 = fig2.line('Date', 'New Deaths', legend_label='Bengkulu', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_bengkulu)
cvdIDJK2 = fig2.line('Date', 'New Deaths', legend_label='DKI Jakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_dki)
cvdIDYO2 = fig2.line('Date', 'New Deaths', legend_label='Daerah Istimewa Yogyakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_diy)
cvdIDGO2 = fig2.line('Date', 'New Deaths', legend_label='Gorontalo', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_gorontalo)
cvdIDN2 = fig2.line('Date', 'New Deaths', legend_label='Indonesia', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_indonesia)
cvdIDJA2 = fig2.line('Date', 'New Deaths', legend_label='Jambi', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jambi)
cvdIDJB2 = fig2.line('Date', 'New Deaths', legend_label='Jawa Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jabar)
cvdIDJT2 = fig2.line('Date', 'New Deaths', legend_label='Jawa Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jateng)
cvdIDJI2 = fig2.line('Date', 'New Deaths', legend_label='Jawa Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_jatim)
cvdIDKB2 = fig2.line('Date', 'New Deaths', legend_label='Kalimantan Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalbar)
cvdIDKS2 = fig2.line('Date', 'New Deaths', legend_label='Kalimantan Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalsel)
cvdIDKT2 = fig2.line('Date', 'New Deaths', legend_label='Kalimantan Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalteng)
cvdIDKI2 = fig2.line('Date', 'New Deaths', legend_label='Kalimantan Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kaltim)
cvdIDKU2 = fig2.line('Date', 'New Deaths', legend_label='Kalimantan Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kalut)
cvdIDBB2 = fig2.line('Date', 'New Deaths', legend_label='Kepulauan Bangka Belitung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kepbangkab)
cvdIDKR2 = fig2.line('Date', 'New Deaths', legend_label='Kepulauan Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_kepriau)
cvdIDLA2 = fig2.line('Date', 'New Deaths', legend_label='Lampung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_lampung)
cvdIDMA2 = fig2.line('Date', 'New Deaths', legend_label='Maluku', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_maluku)
cvdIDMU2 = fig2.line('Date', 'New Deaths', legend_label='Maluku Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_malukut)
cvdIDNB2 = fig2.line('Date', 'New Deaths', legend_label='Nusa Tenggara Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_ntb)
cvdIDNT2 = fig2.line('Date', 'New Deaths', legend_label='Nusa Tenggara Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_ntt)
cvdIDPA2 = fig2.line('Date', 'New Deaths', legend_label='Papua', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_papua)
cvdIDPB2 = fig2.line('Date', 'New Deaths', legend_label='Papua Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_papbar)
cvdIDRI2 = fig2.line('Date', 'New Deaths', legend_label='Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_riau)
cvdIDSR2 = fig2.line('Date', 'New Deaths', legend_label='Sulawesi Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulbar)
cvdIDSN2 = fig2.line('Date', 'New Deaths', legend_label='Sulawesi Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulsel)
cvdIDST2 = fig2.line('Date', 'New Deaths', legend_label='Sulawesi Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulteng)
cvdIDSG2 = fig2.line('Date', 'New Deaths', legend_label='Sulawesi Tenggara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sultengg)
cvdIDSA2 = fig2.line('Date', 'New Deaths', legend_label='Sulawesi Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sulut)
cvdIDSB2 = fig2.line('Date', 'New Deaths', legend_label='Sumatera Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sumbar)
cvdIDSS2 = fig2.line('Date', 'New Deaths', legend_label='Sumatera Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sumsel)
cvdIDSU2 = fig2.line('Date', 'New Deaths', legend_label='Sumatera Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2, source=data_source_sumut)

# interaktif color
pickercvdIDAC2 = ColorPicker(title='set color Aceh',default_size=100)
pickercvdIDAC2.js_link('color', cvdIDAC2.glyph, 'line_color')

pickercvdIDBA2 = ColorPicker(title='set color Bali',default_size=100)
pickercvdIDBA2.js_link('color', cvdIDBA2.glyph, 'line_color')

pickercvdIDBT2 = ColorPicker(title='set color Banten',default_size=100)
pickercvdIDBT2.js_link('color', cvdIDBT2.glyph, 'line_color')

pickercvdIDBE2 = ColorPicker(title='set color Bengkulu',default_size=100)
pickercvdIDBE2.js_link('color', cvdIDBE2.glyph, 'line_color')

pickercvdIDJK2 = ColorPicker(title='set color DKI Jakarta',default_size=100)
pickercvdIDJK2.js_link('color', cvdIDJK2.glyph, 'line_color')

pickercvdIDYO2 = ColorPicker(title='set color Daerah Istimewa Yogyakarta',default_size=100)
pickercvdIDYO2.js_link('color', cvdIDYO2.glyph, 'line_color')

pickercvdIDGO2 = ColorPicker(title='set color Gorontalo',default_size=100)
pickercvdIDGO2.js_link('color', cvdIDGO2.glyph, 'line_color')

pickercvdIDN2 = ColorPicker(title='set color Indonesia',default_size=100)
pickercvdIDN2.js_link('color', cvdIDN2.glyph, 'line_color')

pickercvdIDJA2 = ColorPicker(title='set color Jambi',default_size=100)
pickercvdIDJA2.js_link('color', cvdIDJA2.glyph, 'line_color')

pickercvdIDJB2 = ColorPicker(title='set color Jawa Barat',default_size=100)
pickercvdIDJB2.js_link('color', cvdIDJB2.glyph, 'line_color')

pickercvdIDJT2 = ColorPicker(title='set color Jawa Tengah',default_size=100)
pickercvdIDJT2.js_link('color', cvdIDJT2.glyph, 'line_color')

pickercvdIDJI2 = ColorPicker(title='set color Jawa Timur',default_size=100)
pickercvdIDJI2.js_link('color', cvdIDJI2.glyph, 'line_color')

pickercvdIDKB2 = ColorPicker(title='set color Kalimantan Barat',default_size=100)
pickercvdIDKB2.js_link('color', cvdIDKB2.glyph, 'line_color')

pickercvdIDKS2 = ColorPicker(title='set color Kalimantan Selatan',default_size=100)
pickercvdIDKS2.js_link('color', cvdIDKS2.glyph, 'line_color')

pickercvdIDKT2 = ColorPicker(title='set color Kalimantan Tengah',default_size=100)
pickercvdIDKT2.js_link('color', cvdIDKT2.glyph, 'line_color')

pickercvdIDKI2 = ColorPicker(title='set color Kalimantan Timur',default_size=100)
pickercvdIDKI2.js_link('color', cvdIDKI2.glyph, 'line_color')

pickercvdIDKU2 = ColorPicker(title='set color Kalimantan Utara',default_size=100)
pickercvdIDKU2.js_link('color', cvdIDKU2.glyph, 'line_color')

pickercvdIDBB2 = ColorPicker(title='set color Kepulauan Bangka Belitung',default_size=100)
pickercvdIDBB2.js_link('color', cvdIDBB2.glyph, 'line_color')

pickercvdIDKR2 = ColorPicker(title='set color Kepulauan Riau',default_size=100)
pickercvdIDKR2.js_link('color', cvdIDKR2.glyph, 'line_color')

pickercvdIDLA2 = ColorPicker(title='set color Lampung',default_size=100)
pickercvdIDLA2.js_link('color', cvdIDLA2.glyph, 'line_color')

pickercvdIDMA2 = ColorPicker(title='set color Maluku',default_size=100)
pickercvdIDMA2.js_link('color', cvdIDMA2.glyph, 'line_color')

pickercvdIDMU2 = ColorPicker(title='set color Maluku Utara',default_size=100)
pickercvdIDMU2.js_link('color', cvdIDMU2.glyph, 'line_color')

pickercvdIDNB2 = ColorPicker(title='set color Nusa Tenggara Barat',default_size=100)
pickercvdIDNB2.js_link('color', cvdIDNB2.glyph, 'line_color')

pickercvdIDNT2 = ColorPicker(title='set color Nusa Tenggara Timur',default_size=100)
pickercvdIDNT2.js_link('color', cvdIDNT2.glyph, 'line_color')

pickercvdIDPA2 = ColorPicker(title='set color Papua',default_size=100)
pickercvdIDPA2.js_link('color', cvdIDPA2.glyph, 'line_color')

pickercvdIDPB2 = ColorPicker(title='set color Papua Barat',default_size=100)
pickercvdIDPB2.js_link('color', cvdIDPB2.glyph, 'line_color')

pickercvdIDRI2 = ColorPicker(title='set color Riau',default_size=100)
pickercvdIDRI2.js_link('color', cvdIDRI2.glyph, 'line_color')

pickercvdIDSR2 = ColorPicker(title='set color Sulawesi Barat',default_size=100)
pickercvdIDSR2.js_link('color', cvdIDSR2.glyph, 'line_color')

pickercvdIDSN2 = ColorPicker(title='set color Sulawesi Selatan',default_size=100)
pickercvdIDSN2.js_link('color', cvdIDSN2.glyph, 'line_color')

pickercvdIDST2 = ColorPicker(title='set color Sulawesi Tengah',default_size=100)
pickercvdIDST2.js_link('color', cvdIDST2.glyph, 'line_color')

pickercvdIDSG2 = ColorPicker(title='set color Sulawesi Tenggara',default_size=100)
pickercvdIDSG2.js_link('color', cvdIDSG2.glyph, 'line_color')

pickercvdIDSA2 = ColorPicker(title='set color Sulawesi Utara',default_size=100)
pickercvdIDSA2.js_link('color', cvdIDSA2.glyph, 'line_color')

pickercvdIDSB2 = ColorPicker(title='set color Sumatera Barat',default_size=100)
pickercvdIDSB2.js_link('color', cvdIDSB2.glyph, 'line_color')

pickercvdIDSS2 = ColorPicker(title='set color Sumatera Selatan',default_size=100)
pickercvdIDSS2.js_link('color', cvdIDSS2.glyph, 'line_color')

pickercvdIDSU2 = ColorPicker(title='set color Sumatera Utara',default_size=100)
pickercvdIDSU2.js_link('color', cvdIDSU2.glyph, 'line_color')

tooltips = [('Date','@Date{%F}'), ('Value', '@{New Deaths}')]
formatters = {'@Date':'datetime'}

curdoc().theme = 'dark_minimal'

fig2.add_tools(HoverTool(renderers=[cvdIDAC2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDBA2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDBT2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDBE2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDJK2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDYO2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDGO2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDN2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDJA2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDJB2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDJT2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDJI2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDKB2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDKS2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDKT2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDKI2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDKU2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDBB2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDKR2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDLA2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDMA2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDMU2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDNB2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDNT2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDPA2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDPB2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDRI2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDSR2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDSN2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDST2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDSG2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDSA2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDSB2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDSS2],tooltips=tooltips,formatters=formatters))
fig2.add_tools(HoverTool(renderers=[cvdIDSU2],tooltips=tooltips,formatters=formatters))
fig2.legend.location = 'top_right'
fig2.legend.click_policy='hide'

layout2 = row(fig2,widgetbox(pickercvdIDAC2,pickercvdIDBA2,pickercvdIDBT2,pickercvdIDBE2,pickercvdIDJK2,pickercvdIDYO2,pickercvdIDGO2,pickercvdIDN2,pickercvdIDJA2,pickercvdIDJB2,pickercvdIDJT2,pickercvdIDJI2,pickercvdIDKB2,
                             pickercvdIDKS2,pickercvdIDKT2,pickercvdIDKI2,pickercvdIDKU2,pickercvdIDBB2,pickercvdIDKR2,pickercvdIDLA2,pickercvdIDMA2,pickercvdIDMU2,pickercvdIDNB2,pickercvdIDNT2,pickercvdIDPA2,pickercvdIDPB2,
                             pickercvdIDRI2,pickercvdIDSR2,pickercvdIDSN2,pickercvdIDST2,pickercvdIDSG2,pickercvdIDSA2,pickercvdIDSB2,pickercvdIDSS2,pickercvdIDSU2))
curdoc().add_root(layout2)

select2 = figure(title='Covid-19 (New Deaths)',
        plot_height = 150,
        plot_width=1100,
        y_range=fig2.y_range,
        x_axis_type='datetime',
        tools='',
        x_axis_label='Year',
        y_axis_label='New Deaths',
        toolbar_location =None)
range_tool = RangeTool(x_range=fig2.x_range)
range_tool.overlay.fill_color ='red'
range_tool.overlay.fill_alpha = .2

select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_aceh)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bali)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_banten)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bengkulu)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_dki)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_diy)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_gorontalo)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_indonesia)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jambi)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jabar)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jateng)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jatim)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalbar)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalsel)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalteng)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kaltim)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalut)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepbangkab)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepriau)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_lampung)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_maluku)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_malukut)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntb)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntt)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papua)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papbar)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_riau)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulbar)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulsel)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulteng)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sultengg)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulut)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumbar)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumsel)
select2.line('Date','New Deaths',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumut)


# select2.ygrid.gird_line_color=None
select2.add_tools(range_tool)
select2.toolbar.active_multi=range_tool

layoutsatu = column(select2)
# show(layoutdua)

grid2 = gridplot([[layout2], [layoutsatu]])

#New Recovered
dates3 = np.array(cvdIDAC['Date'])
fig3 = figure(x_axis_type='datetime',
             plot_height=1100, plot_width=1100,
             title='Covid-19 (New Recovered)',
             x_axis_label='Year', y_axis_label='New Recovered',
             x_range =(dates3[100],dates3[200]))

cvdIDAC3 = fig3.line('Date', 'New Recovered', legend_label='Aceh', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_aceh)
cvdIDBA3 = fig3.line('Date', 'New Recovered', legend_label='Bali', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_bali)
cvdIDBT3 = fig3.line('Date', 'New Recovered', legend_label='Banten', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_banten)
cvdIDBE3 = fig3.line('Date', 'New Recovered', legend_label='Bengkulu', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_bengkulu)
cvdIDJK3 = fig3.line('Date', 'New Recovered', legend_label='DKI Jakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_dki)
cvdIDYO3 = fig3.line('Date', 'New Recovered', legend_label='Daerah Istimewa Yogyakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_diy)
cvdIDGO3 = fig3.line('Date', 'New Recovered', legend_label='Gorontalo', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_gorontalo)
cvdIDN3 = fig3.line('Date', 'New Recovered', legend_label='Indonesia', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_indonesia)
cvdIDJA3 = fig3.line('Date', 'New Recovered', legend_label='Jambi', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_jambi)
cvdIDJB3 = fig3.line('Date', 'New Recovered', legend_label='Jawa Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_jabar)
cvdIDJT3 = fig3.line('Date', 'New Recovered', legend_label='Jawa Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_jateng)
cvdIDJI3 = fig3.line('Date', 'New Recovered', legend_label='Jawa Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_jatim)
cvdIDKB3 = fig3.line('Date', 'New Recovered', legend_label='Kalimantan Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_kalbar)
cvdIDKS3 = fig3.line('Date', 'New Recovered', legend_label='Kalimantan Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_kalsel)
cvdIDKT3 = fig3.line('Date', 'New Recovered', legend_label='Kalimantan Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_kalteng)
cvdIDKI3 = fig3.line('Date', 'New Recovered', legend_label='Kalimantan Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_kaltim)
cvdIDKU3 = fig3.line('Date', 'New Recovered', legend_label='Kalimantan Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_kalut)
cvdIDBB3 = fig3.line('Date', 'New Recovered', legend_label='Kepulauan Bangka Belitung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_kepbangkab)
cvdIDKR3 = fig3.line('Date', 'New Recovered', legend_label='Kepulauan Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_kepriau)
cvdIDLA3 = fig3.line('Date', 'New Recovered', legend_label='Lampung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_lampung)
cvdIDMA3 = fig3.line('Date', 'New Recovered', legend_label='Maluku', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_maluku)
cvdIDMU3 = fig3.line('Date', 'New Recovered', legend_label='Maluku Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_malukut)
cvdIDNB3 = fig3.line('Date', 'New Recovered', legend_label='Nusa Tenggara Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_ntb)
cvdIDNT3 = fig3.line('Date', 'New Recovered', legend_label='Nusa Tenggara Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_ntt)
cvdIDPA3 = fig3.line('Date', 'New Recovered', legend_label='Papua', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_papua)
cvdIDPB3 = fig3.line('Date', 'New Recovered', legend_label='Papua Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_papbar)
cvdIDRI3 = fig3.line('Date', 'New Recovered', legend_label='Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_riau)
cvdIDSR3 = fig3.line('Date', 'New Recovered', legend_label='Sulawesi Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sulbar)
cvdIDSN3 = fig3.line('Date', 'New Recovered', legend_label='Sulawesi Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sulsel)
cvdIDST3 = fig3.line('Date', 'New Recovered', legend_label='Sulawesi Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sulteng)
cvdIDSG3 = fig3.line('Date', 'New Recovered', legend_label='Sulawesi Tenggara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sultengg)
cvdIDSA3 = fig3.line('Date', 'New Recovered', legend_label='Sulawesi Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sulut)
cvdIDSB3 = fig3.line('Date', 'New Recovered', legend_label='Sumatera Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sumbar)
cvdIDSS3 = fig3.line('Date', 'New Recovered', legend_label='Sumatera Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sumsel)
cvdIDSU3 = fig3.line('Date', 'New Recovered', legend_label='Sumatera Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=3, source=data_source_sumut)

# interaktif color
pickercvdIDAC3 = ColorPicker(title='set color Aceh',default_size=100)
pickercvdIDAC3.js_link('color', cvdIDAC3.glyph, 'line_color')

pickercvdIDBA3 = ColorPicker(title='set color Bali',default_size=100)
pickercvdIDBA3.js_link('color', cvdIDBA3.glyph, 'line_color')

pickercvdIDBT3 = ColorPicker(title='set color Banten',default_size=100)
pickercvdIDBT3.js_link('color', cvdIDBT3.glyph, 'line_color')

pickercvdIDBE3 = ColorPicker(title='set color Bengkulu',default_size=100)
pickercvdIDBE3.js_link('color', cvdIDBE3.glyph, 'line_color')

pickercvdIDJK3 = ColorPicker(title='set color DKI Jakarta',default_size=100)
pickercvdIDJK3.js_link('color', cvdIDJK3.glyph, 'line_color')

pickercvdIDYO3 = ColorPicker(title='set color Daerah Istimewa Yogyakarta',default_size=100)
pickercvdIDYO3.js_link('color', cvdIDYO3.glyph, 'line_color')

pickercvdIDGO3 = ColorPicker(title='set color Gorontalo',default_size=100)
pickercvdIDGO3.js_link('color', cvdIDGO3.glyph, 'line_color')

pickercvdIDN3 = ColorPicker(title='set color Indonesia',default_size=100)
pickercvdIDN3.js_link('color', cvdIDN3.glyph, 'line_color')

pickercvdIDJA3 = ColorPicker(title='set color Jambi',default_size=100)
pickercvdIDJA3.js_link('color', cvdIDJA3.glyph, 'line_color')

pickercvdIDJB3 = ColorPicker(title='set color Jawa Barat',default_size=100)
pickercvdIDJB3.js_link('color', cvdIDJB3.glyph, 'line_color')

pickercvdIDJT3 = ColorPicker(title='set color Jawa Tengah',default_size=100)
pickercvdIDJT3.js_link('color', cvdIDJT3.glyph, 'line_color')

pickercvdIDJI3 = ColorPicker(title='set color Jawa Timur',default_size=100)
pickercvdIDJI3.js_link('color', cvdIDJI3.glyph, 'line_color')

pickercvdIDKB3 = ColorPicker(title='set color Kalimantan Barat',default_size=100)
pickercvdIDKB3.js_link('color', cvdIDKB3.glyph, 'line_color')

pickercvdIDKS3 = ColorPicker(title='set color Kalimantan Selatan',default_size=100)
pickercvdIDKS3.js_link('color', cvdIDKS3.glyph, 'line_color')

pickercvdIDKT3 = ColorPicker(title='set color Kalimantan Tengah',default_size=100)
pickercvdIDKT3.js_link('color', cvdIDKT3.glyph, 'line_color')

pickercvdIDKI3 = ColorPicker(title='set color Kalimantan Timur',default_size=100)
pickercvdIDKI3.js_link('color', cvdIDKI3.glyph, 'line_color')

pickercvdIDKU3 = ColorPicker(title='set color Kalimantan Utara',default_size=100)
pickercvdIDKU3.js_link('color', cvdIDKU3.glyph, 'line_color')

pickercvdIDBB3 = ColorPicker(title='set color Kepulauan Bangka Belitung',default_size=100)
pickercvdIDBB3.js_link('color', cvdIDBB3.glyph, 'line_color')

pickercvdIDKR3 = ColorPicker(title='set color Kepulauan Riau',default_size=100)
pickercvdIDKR3.js_link('color', cvdIDKR3.glyph, 'line_color')

pickercvdIDLA3 = ColorPicker(title='set color Lampung',default_size=100)
pickercvdIDLA3.js_link('color', cvdIDLA3.glyph, 'line_color')

pickercvdIDMA3 = ColorPicker(title='set color Maluku',default_size=100)
pickercvdIDMA3.js_link('color', cvdIDMA3.glyph, 'line_color')

pickercvdIDMU3 = ColorPicker(title='set color Maluku Utara',default_size=100)
pickercvdIDMU3.js_link('color', cvdIDMU3.glyph, 'line_color')

pickercvdIDNB3 = ColorPicker(title='set color Nusa Tenggara Barat',default_size=100)
pickercvdIDNB3.js_link('color', cvdIDNB3.glyph, 'line_color')

pickercvdIDNT3 = ColorPicker(title='set color Nusa Tenggara Timur',default_size=100)
pickercvdIDNT3.js_link('color', cvdIDNT3.glyph, 'line_color')

pickercvdIDPA3 = ColorPicker(title='set color Papua',default_size=100)
pickercvdIDPA3.js_link('color', cvdIDPA3.glyph, 'line_color')

pickercvdIDPB3 = ColorPicker(title='set color Papua Barat',default_size=100)
pickercvdIDPB3.js_link('color', cvdIDPB3.glyph, 'line_color')

pickercvdIDRI3 = ColorPicker(title='set color Riau',default_size=100)
pickercvdIDRI3.js_link('color', cvdIDRI3.glyph, 'line_color')

pickercvdIDSR3 = ColorPicker(title='set color Sulawesi Barat',default_size=100)
pickercvdIDSR3.js_link('color', cvdIDSR3.glyph, 'line_color')

pickercvdIDSN3 = ColorPicker(title='set color Sulawesi Selatan',default_size=100)
pickercvdIDSN3.js_link('color', cvdIDSN3.glyph, 'line_color')

pickercvdIDST3 = ColorPicker(title='set color Sulawesi Tengah',default_size=100)
pickercvdIDST3.js_link('color', cvdIDST3.glyph, 'line_color')

pickercvdIDSG3 = ColorPicker(title='set color Sulawesi Tenggara',default_size=100)
pickercvdIDSG3.js_link('color', cvdIDSG3.glyph, 'line_color')

pickercvdIDSA3 = ColorPicker(title='set color Sulawesi Utara',default_size=100)
pickercvdIDSA3.js_link('color', cvdIDSA3.glyph, 'line_color')

pickercvdIDSB3 = ColorPicker(title='set color Sumatera Barat',default_size=100)
pickercvdIDSB3.js_link('color', cvdIDSB3.glyph, 'line_color')

pickercvdIDSS3 = ColorPicker(title='set color Sumatera Selatan',default_size=100)
pickercvdIDSS3.js_link('color', cvdIDSS3.glyph, 'line_color')

pickercvdIDSU3 = ColorPicker(title='set color Sumatera Utara',default_size=100)
pickercvdIDSU3.js_link('color', cvdIDSU3.glyph, 'line_color')

tooltips = [('Date','@Date{%F}'), ('Value', '@{New Recovered}')]
formatters = {'@Date':'datetime'}

curdoc().theme = 'dark_minimal'

fig3.add_tools(HoverTool(renderers=[cvdIDAC3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDBA3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDBT3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDBE3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDJK3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDYO3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDGO3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDN3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDJA3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDJB3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDJT3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDJI3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDKB3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDKS3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDKT3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDKI3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDKU3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDBB3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDKR3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDLA3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDMA3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDMU3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDNB3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDNT3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDPA3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDPB3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDRI3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDSR3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDSN3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDST3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDSG3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDSA3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDSB3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDSS3],tooltips=tooltips,formatters=formatters))
fig3.add_tools(HoverTool(renderers=[cvdIDSU3],tooltips=tooltips,formatters=formatters))
fig3.legend.location = 'top_right'
fig3.legend.click_policy='hide'

layout3 = row(fig3,widgetbox(pickercvdIDAC3,pickercvdIDBA3,pickercvdIDBT3,pickercvdIDBE3,pickercvdIDJK3,pickercvdIDYO3,pickercvdIDGO3,pickercvdIDN3,pickercvdIDJA3,pickercvdIDJB3,pickercvdIDJT3,pickercvdIDJI3,pickercvdIDKB3,
                             pickercvdIDKS3,pickercvdIDKT3,pickercvdIDKI3,pickercvdIDKU3,pickercvdIDBB3,pickercvdIDKR3,pickercvdIDLA3,pickercvdIDMA3,pickercvdIDMU3,pickercvdIDNB3,pickercvdIDNT3,pickercvdIDPA3,pickercvdIDPB3,
                             pickercvdIDRI3,pickercvdIDSR3,pickercvdIDSN3,pickercvdIDST3,pickercvdIDSG3,pickercvdIDSA3,pickercvdIDSB3,pickercvdIDSS3,pickercvdIDSU3))
curdoc().add_root(layout3)

select3 = figure(title='Covid-19 (New Recovered)',
        plot_height = 150,
        plot_width=1100,
        y_range=fig3.y_range,
        x_axis_type='datetime',
        tools='',
        x_axis_label='Year',
        y_axis_label='New Recovered',
        toolbar_location =None)
range_tool = RangeTool(x_range=fig3.x_range)
range_tool.overlay.fill_color ='red'
range_tool.overlay.fill_alpha = .2

select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_aceh)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bali)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_banten)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bengkulu)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_dki)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_diy)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_gorontalo)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_indonesia)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jambi)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jabar)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jateng)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jatim)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalbar)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalsel)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalteng)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kaltim)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalut)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepbangkab)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepriau)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_lampung)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_maluku)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_malukut)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntb)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntt)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papua)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papbar)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_riau)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulbar)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulsel)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulteng)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sultengg)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulut)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumbar)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumsel)
select3.line('Date','New Recovered',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumut)


# select3.ygrid.gird_line_color=None
select3.add_tools(range_tool)
select3.toolbar.active_multi=range_tool

layoutsatu = column(select3)
# show(layoutdua)

grid3 = gridplot([[layout3], [layoutsatu]])

#New Active Cases
dates4 = np.array(cvdIDAC['Date'])
fig4 = figure(x_axis_type='datetime',
             plot_height=1400, plot_width=1100,
             title='Covid-19 (New Active Cases)',
             x_axis_label='Year', y_axis_label='New Active Cases',
             x_range =(dates4[100],dates4[200]))

cvdIDAC4 = fig4.line('Date', 'New Active Cases', legend_label='Aceh', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_aceh)
cvdIDBA4 = fig4.line('Date', 'New Active Cases', legend_label='Bali', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_bali)
cvdIDBT4 = fig4.line('Date', 'New Active Cases', legend_label='Banten', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_banten)
cvdIDBE4 = fig4.line('Date', 'New Active Cases', legend_label='Bengkulu', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_bengkulu)
cvdIDJK4 = fig4.line('Date', 'New Active Cases', legend_label='DKI Jakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_dki)
cvdIDYO4 = fig4.line('Date', 'New Active Cases', legend_label='Daerah Istimewa Yogyakarta', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_diy)
cvdIDGO4 = fig4.line('Date', 'New Active Cases', legend_label='Gorontalo', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_gorontalo)
cvdIDN4 = fig4.line('Date', 'New Active Cases', legend_label='Indonesia', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_indonesia)
cvdIDJA4 = fig4.line('Date', 'New Active Cases', legend_label='Jambi', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_jambi)
cvdIDJB4 = fig4.line('Date', 'New Active Cases', legend_label='Jawa Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_jabar)
cvdIDJT4 = fig4.line('Date', 'New Active Cases', legend_label='Jawa Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_jateng)
cvdIDJI4 = fig4.line('Date', 'New Active Cases', legend_label='Jawa Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_jatim)
cvdIDKB4 = fig4.line('Date', 'New Active Cases', legend_label='Kalimantan Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_kalbar)
cvdIDKS4 = fig4.line('Date', 'New Active Cases', legend_label='Kalimantan Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_kalsel)
cvdIDKT4 = fig4.line('Date', 'New Active Cases', legend_label='Kalimantan Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_kalteng)
cvdIDKI4 = fig4.line('Date', 'New Active Cases', legend_label='Kalimantan Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_kaltim)
cvdIDKU4 = fig4.line('Date', 'New Active Cases', legend_label='Kalimantan Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_kalut)
cvdIDBB4 = fig4.line('Date', 'New Active Cases', legend_label='Kepulauan Bangka Belitung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_kepbangkab)
cvdIDKR4 = fig4.line('Date', 'New Active Cases', legend_label='Kepulauan Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_kepriau)
cvdIDLA4 = fig4.line('Date', 'New Active Cases', legend_label='Lampung', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_lampung)
cvdIDMA4 = fig4.line('Date', 'New Active Cases', legend_label='Maluku', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_maluku)
cvdIDMU4 = fig4.line('Date', 'New Active Cases', legend_label='Maluku Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_malukut)
cvdIDNB4 = fig4.line('Date', 'New Active Cases', legend_label='Nusa Tenggara Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_ntb)
cvdIDNT4 = fig4.line('Date', 'New Active Cases', legend_label='Nusa Tenggara Timur', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_ntt)
cvdIDPA4 = fig4.line('Date', 'New Active Cases', legend_label='Papua', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_papua)
cvdIDPB4 = fig4.line('Date', 'New Active Cases', legend_label='Papua Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_papbar)
cvdIDRI4 = fig4.line('Date', 'New Active Cases', legend_label='Riau', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_riau)
cvdIDSR4 = fig4.line('Date', 'New Active Cases', legend_label='Sulawesi Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sulbar)
cvdIDSN4 = fig4.line('Date', 'New Active Cases', legend_label='Sulawesi Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sulsel)
cvdIDST4 = fig4.line('Date', 'New Active Cases', legend_label='Sulawesi Tengah', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sulteng)
cvdIDSG4 = fig4.line('Date', 'New Active Cases', legend_label='Sulawesi Tenggara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sultengg)
cvdIDSA4 = fig4.line('Date', 'New Active Cases', legend_label='Sulawesi Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sulut)
cvdIDSB4 = fig4.line('Date', 'New Active Cases', legend_label='Sumatera Barat', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sumbar)
cvdIDSS4 = fig4.line('Date', 'New Active Cases', legend_label='Sumatera Selatan', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sumsel)
cvdIDSU4 = fig4.line('Date', 'New Active Cases', legend_label='Sumatera Utara', color='#%06x' % random.randint(0, 0xFFFFFF),line_width=4, source=data_source_sumut)

# interaktif color
pickercvdIDAC4 = ColorPicker(title='set color Aceh',default_size=100)
pickercvdIDAC4.js_link('color', cvdIDAC4.glyph, 'line_color')

pickercvdIDBA4 = ColorPicker(title='set color Bali',default_size=100)
pickercvdIDBA4.js_link('color', cvdIDBA4.glyph, 'line_color')

pickercvdIDBT4 = ColorPicker(title='set color Banten',default_size=100)
pickercvdIDBT4.js_link('color', cvdIDBT4.glyph, 'line_color')

pickercvdIDBE4 = ColorPicker(title='set color Bengkulu',default_size=100)
pickercvdIDBE4.js_link('color', cvdIDBE4.glyph, 'line_color')

pickercvdIDJK4 = ColorPicker(title='set color DKI Jakarta',default_size=100)
pickercvdIDJK4.js_link('color', cvdIDJK4.glyph, 'line_color')

pickercvdIDYO4 = ColorPicker(title='set color Daerah Istimewa Yogyakarta',default_size=100)
pickercvdIDYO4.js_link('color', cvdIDYO4.glyph, 'line_color')

pickercvdIDGO4 = ColorPicker(title='set color Gorontalo',default_size=100)
pickercvdIDGO4.js_link('color', cvdIDGO4.glyph, 'line_color')

pickercvdIDN4 = ColorPicker(title='set color Indonesia',default_size=100)
pickercvdIDN4.js_link('color', cvdIDN4.glyph, 'line_color')

pickercvdIDJA4 = ColorPicker(title='set color Jambi',default_size=100)
pickercvdIDJA4.js_link('color', cvdIDJA4.glyph, 'line_color')

pickercvdIDJB4 = ColorPicker(title='set color Jawa Barat',default_size=100)
pickercvdIDJB4.js_link('color', cvdIDJB4.glyph, 'line_color')

pickercvdIDJT4 = ColorPicker(title='set color Jawa Tengah',default_size=100)
pickercvdIDJT4.js_link('color', cvdIDJT4.glyph, 'line_color')

pickercvdIDJI4 = ColorPicker(title='set color Jawa Timur',default_size=100)
pickercvdIDJI4.js_link('color', cvdIDJI4.glyph, 'line_color')

pickercvdIDKB4 = ColorPicker(title='set color Kalimantan Barat',default_size=100)
pickercvdIDKB4.js_link('color', cvdIDKB4.glyph, 'line_color')

pickercvdIDKS4 = ColorPicker(title='set color Kalimantan Selatan',default_size=100)
pickercvdIDKS4.js_link('color', cvdIDKS4.glyph, 'line_color')

pickercvdIDKT4 = ColorPicker(title='set color Kalimantan Tengah',default_size=100)
pickercvdIDKT4.js_link('color', cvdIDKT4.glyph, 'line_color')

pickercvdIDKI4 = ColorPicker(title='set color Kalimantan Timur',default_size=100)
pickercvdIDKI4.js_link('color', cvdIDKI4.glyph, 'line_color')

pickercvdIDKU4 = ColorPicker(title='set color Kalimantan Utara',default_size=100)
pickercvdIDKU4.js_link('color', cvdIDKU4.glyph, 'line_color')

pickercvdIDBB4 = ColorPicker(title='set color Kepulauan Bangka Belitung',default_size=100)
pickercvdIDBB4.js_link('color', cvdIDBB4.glyph, 'line_color')

pickercvdIDKR4 = ColorPicker(title='set color Kepulauan Riau',default_size=100)
pickercvdIDKR4.js_link('color', cvdIDKR4.glyph, 'line_color')

pickercvdIDLA4 = ColorPicker(title='set color Lampung',default_size=100)
pickercvdIDLA4.js_link('color', cvdIDLA4.glyph, 'line_color')

pickercvdIDMA4 = ColorPicker(title='set color Maluku',default_size=100)
pickercvdIDMA4.js_link('color', cvdIDMA4.glyph, 'line_color')

pickercvdIDMU4 = ColorPicker(title='set color Maluku Utara',default_size=100)
pickercvdIDMU4.js_link('color', cvdIDMU4.glyph, 'line_color')

pickercvdIDNB4 = ColorPicker(title='set color Nusa Tenggara Barat',default_size=100)
pickercvdIDNB4.js_link('color', cvdIDNB4.glyph, 'line_color')

pickercvdIDNT4 = ColorPicker(title='set color Nusa Tenggara Timur',default_size=100)
pickercvdIDNT4.js_link('color', cvdIDNT4.glyph, 'line_color')

pickercvdIDPA4 = ColorPicker(title='set color Papua',default_size=100)
pickercvdIDPA4.js_link('color', cvdIDPA4.glyph, 'line_color')

pickercvdIDPB4 = ColorPicker(title='set color Papua Barat',default_size=100)
pickercvdIDPB4.js_link('color', cvdIDPB4.glyph, 'line_color')

pickercvdIDRI4 = ColorPicker(title='set color Riau',default_size=100)
pickercvdIDRI4.js_link('color', cvdIDRI4.glyph, 'line_color')

pickercvdIDSR4 = ColorPicker(title='set color Sulawesi Barat',default_size=100)
pickercvdIDSR4.js_link('color', cvdIDSR4.glyph, 'line_color')

pickercvdIDSN4 = ColorPicker(title='set color Sulawesi Selatan',default_size=100)
pickercvdIDSN4.js_link('color', cvdIDSN4.glyph, 'line_color')

pickercvdIDST4 = ColorPicker(title='set color Sulawesi Tengah',default_size=100)
pickercvdIDST4.js_link('color', cvdIDST4.glyph, 'line_color')

pickercvdIDSG4 = ColorPicker(title='set color Sulawesi Tenggara',default_size=100)
pickercvdIDSG4.js_link('color', cvdIDSG4.glyph, 'line_color')

pickercvdIDSA4 = ColorPicker(title='set color Sulawesi Utara',default_size=100)
pickercvdIDSA4.js_link('color', cvdIDSA4.glyph, 'line_color')

pickercvdIDSB4 = ColorPicker(title='set color Sumatera Barat',default_size=100)
pickercvdIDSB4.js_link('color', cvdIDSB4.glyph, 'line_color')

pickercvdIDSS4 = ColorPicker(title='set color Sumatera Selatan',default_size=100)
pickercvdIDSS4.js_link('color', cvdIDSS4.glyph, 'line_color')

pickercvdIDSU4 = ColorPicker(title='set color Sumatera Utara',default_size=100)
pickercvdIDSU4.js_link('color', cvdIDSU4.glyph, 'line_color')

tooltips = [('Date','@Date{%F}'), ('Value', '@{New Active Cases}')]
formatters = {'@Date':'datetime'}

curdoc().theme = 'dark_minimal'

fig4.add_tools(HoverTool(renderers=[cvdIDAC4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDBA4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDBT4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDBE4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDJK4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDYO4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDGO4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDN4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDJA4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDJB4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDJT4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDJI4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDKB4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDKS4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDKT4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDKI4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDKU4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDBB4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDKR4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDLA4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDMA4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDMU4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDNB4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDNT4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDPA4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDPB4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDRI4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDSR4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDSN4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDST4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDSG4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDSA4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDSB4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDSS4],tooltips=tooltips,formatters=formatters))
fig4.add_tools(HoverTool(renderers=[cvdIDSU4],tooltips=tooltips,formatters=formatters))
fig4.legend.location = 'top_right'
fig4.legend.click_policy='hide'

layout4 = row(fig4,widgetbox(pickercvdIDAC4,pickercvdIDBA4,pickercvdIDBT4,pickercvdIDBE4,pickercvdIDJK4,pickercvdIDYO4,pickercvdIDGO4,pickercvdIDN4,pickercvdIDJA4,pickercvdIDJB4,pickercvdIDJT4,pickercvdIDJI4,pickercvdIDKB4,
                             pickercvdIDKS4,pickercvdIDKT4,pickercvdIDKI4,pickercvdIDKU4,pickercvdIDBB4,pickercvdIDKR4,pickercvdIDLA4,pickercvdIDMA4,pickercvdIDMU4,pickercvdIDNB4,pickercvdIDNT4,pickercvdIDPA4,pickercvdIDPB4,
                             pickercvdIDRI4,pickercvdIDSR4,pickercvdIDSN4,pickercvdIDST4,pickercvdIDSG4,pickercvdIDSA4,pickercvdIDSB4,pickercvdIDSS4,pickercvdIDSU4))
curdoc().add_root(layout4)

select4 = figure(title='Covid-19 (New Active Cases)',
        plot_height = 150,
        plot_width=1100,
        y_range=fig4.y_range,
        x_axis_type='datetime',
        tools='',
        x_axis_label='Year',
        y_axis_label='New Active Cases',
        toolbar_location =None)
range_tool = RangeTool(x_range=fig4.x_range)
range_tool.overlay.fill_color ='red'
range_tool.overlay.fill_alpha = .2

select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_aceh)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bali)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_banten)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_bengkulu)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_dki)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_diy)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_gorontalo)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_indonesia)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jambi)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jabar)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jateng)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_jatim)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalbar)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalsel)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalteng)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kaltim)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kalut)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepbangkab)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_kepriau)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_lampung)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_maluku)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_malukut)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntb)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_ntt)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papua)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_papbar)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_riau)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulbar)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulsel)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulteng)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sultengg)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sulut)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumbar)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumsel)
select4.line('Date','New Active Cases',color='#%06x' % random.randint(0, 0xFFFFFF),line_width=2,source=data_source_sumut)


# select4.ygrid.gird_line_color=None
select4.add_tools(range_tool)
select4.toolbar.active_multi=range_tool

layoutsatu = column(select4)
# show(layoutdua)

grid4 = gridplot([[layout4], [layoutsatu]])

#all
tab_newcase = Panel(child=grid1,title='New Cases')
tab_newdeath = Panel(child=grid2,title='New Deaths')
tab_newrecovered = Panel(child=grid3,title='New Recovered')
tab_newactivecases = Panel(child=grid4,title='New Active Cases')

output_file('result.html')

tabs = Tabs(tabs=[tab_newcase,tab_newdeath,tab_newrecovered,tab_newactivecases])

show(tabs)