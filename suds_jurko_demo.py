#!/usr/bin/env python
# coding: utf-8
#

from suds.client import Client

if __name__ == "__main__":
    url = "http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"
    client = Client(url)
    print(client)
