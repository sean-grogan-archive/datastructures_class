#!/usr/bin/env python
from __future__ import division
 
global revrate, corrate
 
def rev_inc(is_dict_name):
 
	if is_dict_name['istryr3'] < is_dict_name['istryr2'] < is_dict_name['istryr1']:
		print '\n     Revenue is increasing!'
	else:
		print '\n     Revenue is inconsistent!'
	   
def rev_rate(is_dict_name):
	global revrate
	rate1 = ((is_dict_name['istryr2'] / is_dict_name['istryr3'])-1)
	rate2 = ((is_dict_name['istryr1'] / is_dict_name['istryr2'])-1)
	revrate = ((rate1 + rate2)/2)*100
	print '\n     Average 3yr revenue growth rate is: ' + str(round(revrate, 4)) + "%"
 
def cor_rate(is_dict_name):
	global corrate
	rate1 = ((is_dict_name['iscoryr2'] / is_dict_name['iscoryr3'])-1)
	rate2 = ((is_dict_name['iscoryr1'] / is_dict_name['iscoryr2'])-1)
	corrate = ((rate1 + rate2)/2)*100
	print '\n     Average 3yr cost of revenue growth rate is: ' + str(round(corrate, 4)) + "%"
 
def analyze_rev_rates(is_dict_name):
	global revrate, corrate
	if revrate > corrate:
		print '\n     Revenue growth rate > cost of revenue growth rate.'
		print '     This could be a good sign!'
	elif revrate == corrate:
		print '\n     Revenue growth rate = cost of revenue growth rate.'
		print '     This could be a bad sign!'
	else:
		print '\n     Revenue growth rate < cost of revenue growth rate.'
		print '     This could be a bad sign!'
 
def inc_inc(is_dict_name):
 
	if is_dict_name['isniyr3'] < is_dict_name['isniyr2'] < is_dict_name['isniyr1']:
		print '\n     Net income is increasing!'
	else:
		print '\n     Net income is inconsistent.'
 
def cash_on_hand(bs_dict_name):
 
	if bs_dict_name['bscceyr1'] == 0 and bs_dict_name['bscceyr1'] == 0 and bs_dict_name['bscceyr1'] == 0:
		print '\n     Company has no cash!'
	else:
		print '\n     Company has cash on hand!'
		cash_inc(bs_dict_name)
 
def cash_inc(bs_dict_name):
 
	if bs_dict_name['bscceyr3'] < bs_dict_name['bscceyr2'] < bs_dict_name['bscceyr1']:
		print '\n     Cash is increasing!'
	else:
		print '\n     Cash balance is inconsistent.'
 
def pos_se(bs_dict_name):
 
	avg_tse = (bs_dict_name['bstseyr1'] + bs_dict_name['bstseyr2'] + bs_dict_name['bstseyr3'])/3
	if avg_tse > 0:
		if bs_dict_name['bstseyr3'] < bs_dict_name['bstseyr2'] < bs_dict_name['bstseyr1']:
			print '\n     Stockholders\' equity is increasing and positive on average! ($' + str(round(avg_tse, 2)) + ')'
		else:
			print '\n     Stockholders\' equity is inconsistent but positive on average ($' + str(round(avg_tse, 2)) + ')'
	elif avg_tse == 0:
		print '\n     Stockholders\' equity is ZERO'
	else:
		print '\n     Average stockolders\' equity is NEGATIVE!'
 
def pos_nta(bs_dict_name):
 
	avg_nta = (bs_dict_name['bsntayr1'] + bs_dict_name['bsntayr2'] + bs_dict_name['bsntayr3'])/3
	if avg_nta > 0:
		if bs_dict_name['bsntayr3'] < bs_dict_name['bsntayr2'] < bs_dict_name['bsntayr1']:
			print '\n     Net tangible assets are increasing and positive on average! ($' + str(round(avg_nta, 2)) + ')'
		else:
			print '\n     Net tangible assets are inconsistent but positive on average ($' + str(round(avg_nta, 2)) + ')'
	elif avg_nta == 0:
		print '\n     Net tangible assets are ZERO'
	else:
		print '\n     Average net tangible assets is NEGATIVE!'
 
def cce(cf_dict_name):
	avg_ccce = (cf_dict_name['cfccceyr1'] + cf_dict_name['cfccceyr2'] + cf_dict_name['cfccceyr3'])/3
	if avg_ccce > 0:
		if cf_dict_name['cfccceyr3'] < cf_dict_name['cfccceyr2'] < cf_dict_name['cfccceyr1']:
			print '\n     Change in cash and cash equivalents is increasing and positive on average! ($' + str(round(avg_ccce, 2)) + ')'
		else:
			print '\n     Change in cash and cash equivalents is inconsistent but positive on average ($' + str(round(avg_ccce, 2)) + ')'
	elif avg_ccce == 0:
		print '\n     Average change in cash and cash equivalents is ZERO'
	else:
		print '\n     Average change in cash and cash equivalents is NEGATIVE! ($' + str(round(avg_ccce, 2)) + ')'
 
def ocf_rev_ratio(cf_dict_name, is_dict_name):
	ratio1 = cf_dict_name['cftcfoayr1'] / is_dict_name['istryr1']
	ratio2 = cf_dict_name['cftcfoayr2'] / is_dict_name['istryr2']
	ratio3 = cf_dict_name['cftcfoayr3'] / is_dict_name['istryr3']
	avg_ratio = (ratio1 + ratio2 + ratio3)/3
	print '\n     On average, company converts ' + str(round((avg_ratio)*100, 2)) + '% of revenue \n     to operating cash flow.'
	if ratio1 > ratio2 > ratio3:
		print '\n     Operating cash flow to revenue ratio is increasing! (' + str(round((ratio3)*100, 2)) + '% --> ' + str(round((ratio2)*100, 2)) + '% --> ' + str(round((ratio1)*100, 2)) + '%)'
	elif ratio3 > ratio2 > ratio1:
		print '\n     Operating cash flow to revenue ratio is decreasing! (' + str(round((ratio3)*100, 2)) + '% --> ' + str(round((ratio2)*100, 2)) + '% --> ' + str(round((ratio1)*100, 2)) + '%)'
	else:
		print '\n     Operating cash flow to revenue ratio is inconsistent. (' + str(round((ratio3)*100, 2)) + '% --> ' + str(round((ratio2)*100, 2)) + '% --> ' + str(round((ratio1)*100, 2)) + '%)'
 
def fcf_analysis(cf_dict_name, is_dict_name):
   
	##  Analyze average FCF
   
	fcf1 = cf_dict_name['cftcfoayr1'] - abs(cf_dict_name['cfceyr1'])
	fcf2 = cf_dict_name['cftcfoayr2'] - abs(cf_dict_name['cfceyr2'])
	fcf3 = cf_dict_name['cftcfoayr3'] - abs(cf_dict_name['cfceyr3'])
	avg_fcf = (fcf1 + fcf2 + fcf3)/3
	print '\n     Average 3yr free cash flow was $' + str(round(avg_fcf, 2)) + '.'
	if fcf1 > fcf2 > fcf3:
		print '\n     Free cash flow is increasing! ($' + str(round(fcf3, 2)) + ' --> $' + str(round(fcf2, 2)) + ' --> $' + str(round(fcf1, 2)) + ')'
	elif fcf3 > fcf2 > fcf1:
		print '\n     Free cash flow is decreasing! ($' + str(round(fcf3, 2)) + ' --> $' + str(round(fcf2, 2)) + ' --> $' + str(round(fcf1, 2)) + ')'
	else:
		print '\n     Free cash flow is inconsistent. ($' + str(round(fcf3, 2)) + ' --> $' + str(round(fcf2, 2)) + ' --> $' + str(round(fcf1, 2)) + ')'
 
	##  Analyze FCF:OCF ratio
	   
	ratio1 = fcf1 / cf_dict_name['cftcfoayr1']
	ratio2 = fcf2 / cf_dict_name['cftcfoayr2']
	ratio3 = fcf3 / cf_dict_name['cftcfoayr3']
	avg_ratio = (ratio1 + ratio2 + ratio3)/3
	if avg_ratio <= 0:
		print '\n     On average, ' + str(round((avg_ratio)*100, 2)) + '% of operating cash flow \n     is free cash flow. This could be a bad sign.'
	else:
		print '\n     On average, ' + str(round((avg_ratio)*100, 2)) + '% of operating cash flow \n     is free cash flow.'
 
	##  Analyze FCF:Rev ratio
	   
	ratio1 = fcf1 / is_dict_name['istryr1']
	ratio2 = fcf2 / is_dict_name['istryr2']
	ratio3 = fcf3 / is_dict_name['istryr3']
	avg_ratio = (ratio1 + ratio2 + ratio3)/3
	print '\n     On average, company converts ' + str(round((avg_ratio)*100, 2)) + '% of revenue \n     to free cash flow.'
	if ratio1 > ratio2 > ratio3:
		print '\n     Free cash flow to revenue ratio is increasing! (' + str(round((ratio3)*100, 2)) + '% --> ' + str(round((ratio2)*100, 2)) + '% --> ' + str(round((ratio1)*100, 2)) + '%)'
	elif ratio3 > ratio2 > ratio1:
		print '\n     Free cash flow to revenue ratio is decreasing! (' + str(round((ratio3)*100, 2)) + '% --> ' + str(round((ratio2)*100, 2)) + '% --> ' + str(round((ratio1)*100, 2)) + '%)'
	else:
		print '\n     Free cash flow to revenue ratio is inconsistent. (' + str(round((ratio3)*100, 2)) + '% --> ' + str(round((ratio2)*100, 2)) + '% --> ' + str(round((ratio1)*100, 2)) + '%)'
