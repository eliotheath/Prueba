#Author: Mr.R Heathcliff
#Wichtig zu beachten The Zen Of Python
#12th: There should be one-- and preferably only one --obvious way to do it.

#!/usr/bin/python
#!python
#-*- coding: utf-8 -*-

#__all__ = ['xbrl']
__version__ = '1.0'

#!/usr/bin/python
#!python

import os                               #Conexion con el SO
import numpy as np                      #NumericalPython
import re                               #RegGex
import pandas as pd                     #Manejo de DataFrame
from functools import reduce

import xmltodict                        #Transformar un XML a un dictionary
import xml.etree.ElementTree as ET      #Leer XML

from bs4 import *                       #Scraping

'''class xbrl:                        #Definicion de clases
    """"Docstring for ClassName"""

    def __init(self,arg):
        super(xbrl,self).__init__()
        self.arg = arg'''


'''Fucniones para leer un XML'''

# == Leer  las etqiuetas de un Xml ==
def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)
# == Pasar las etiquetas a un dictionary
def xmltodf(etiqueta):
    claves=[]
    valores=[]
    for key, value in recursive_items(etiqueta):
        claves.append(key)
        valores.append(value)
    dictionary = dict(zip(claves, valores))
    return dictionary

    '''Creacion de DataFRame's, a partir de la informaicon en las etiquertas'''
#== Si lo quisieras correr desde Atom o Spyder, este es un ejemplo
#path = '/home/rvelez/Projects/Githubeliot/Insumos_Bancos/BMV INSUMOS/FMTY/FMTY/xbrl/ifrsxbrl_812752_2017-04D_1_xbrl.xml'
#path = '/home/rvelez/Projects/Githubeliot/Insumos_Bancos/BMV INSUMOS/FMTY/FMTY/xbrl/ifrsxbrl_826463_2018-01_1_xbrl.xml'
def rep(path):

    with open(path, encoding="ISO-8859-1") as fl:
        doc = xmltodict.parse(fl.read(),dict_constructor = dict)


    #== DataFRame de todas las equiteas
    df1 = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['xbrli:context']])
    # === DataFrame's de los distintos campos de la base de datos ===

    # = Estado de situacion finaciera (sinopsis) ==
    # = Activos (sinopsis)
    # = Activos circulantes (sinopsis)
    a = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CashAndCashEquivalents']])[:2]
    b = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:TradeAndOtherCurrentReceivables']])
    c = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentTaxAssetsCurrent']])
    d = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherCurrentFinancialAssets']])
    e = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:Inventories']])
    f = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentBiologicalAssets']])
    g = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherCurrentNonfinancialAssets']])
    h = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners']])
    i = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners']])
    j = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentAssets']])

    # == Activos no circulantes [Sinopsis]

    k = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentReceivables']])
    l = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentTaxAssetsNoncurrent']])
    m = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentInventories']])
    n = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentBiologicalAssets']])
    o = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherNoncurrentFinancialAssets']])
    p = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:InvestmentAccountedForUsingEquityMethod']])
    q = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:InvestmentsInSubsidiariesJointVenturesAndAssociates']])
    r = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:PropertyPlantAndEquipment']])
    s = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:InvestmentProperty']])
    t = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:Goodwill']])
    u = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:IntangibleAssetsOtherThanGoodwill']])
    v = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:DeferredTaxAssets']])
    w = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherNoncurrentNonfinancialAssets']])
    x = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentAssets']])
    y = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:Assets']])

    # == Capital Contable y Pasivos [sinopsis]
    # == Pasivos [sinopsis]
    # == Pasivos Circulantes [sinopsis]

    z = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:TradeAndOtherCurrentPayables']])
    aa = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentTaxLiabilitiesCurrent']])
    ab = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherCurrentFinancialLiabilities']])
    ac = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherCurrentNonfinancialLiabilities']])

    # == Provisiones circulantes [sinopsis]

    ad = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentProvisionsForEmployeeBenefits']])
    ae = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherShorttermProvisions']])
    af = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentProvisions']])
    ag = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale']])
    ah = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:LiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale']])
    ai = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentLiabilities']])

    # == Pasivos a largo plazo [sinopsis]

    aj = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentPayables']])
    ak = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:CurrentTaxLiabilitiesNoncurrent']])
    al = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherNoncurrentFinancialLiabilities']])
    am = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherNoncurrentNonfinancialLiabilities']])

    # == Provisiones a largo plazo [sinopsis]

    an = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentProvisionsForEmployeeBenefits']])
    ao = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherLongtermProvisions']])
    ap = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentProvisions']])
    aq = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:DeferredTaxLiabilities']])
    ar = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncurrentLiabilities']])
    aS = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:Liabilities']])

    # == Capital Contable [sinopsis]

    at = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:IssuedCapital']])
    au = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:SharePremium']])
    av = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:TreasuryShares']])
    aw = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:RetainedEarnings']])
    ax = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:OtherReserves']])
    ay = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:EquityAttributableToOwnersOfParent']])
    az = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:NoncontrollingInterests']])
    ba = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:Equity']])[:2]
    bb = pd.DataFrame([xmltodf(y) for y in doc['xbrli:xbrl']['ifrs-full:EquityAndLiabilities']])



    R = pd.concat([a,b,c,d,e,f,g,h,i,j,
           k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,
           z,aa,ab,ac,
           ad,ae,af,ag,ah,ai,
           aj,ak,al,am,
           an,ao,ap,aq,ar,aS,
           at,au,av,aw,ax,ay,az,ba,bb]).reset_index()


    R.to_csv('R.csv')
    return R

'''if __name__ == '__main__':          # Cuerpo pirincipal.
    rep(path)'''
