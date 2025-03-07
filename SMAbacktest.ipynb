{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Libraries\n",
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class SMABacktester():\n",
    "    def __init__(self, symbol, SMA_S, SMA_L, start, end):\n",
    "        self.symbol = symbol\n",
    "        self.SMA_S = SMA_S\n",
    "        self.SMA_L = SMA_L\n",
    "        self.start = start\n",
    "        self.end = end\n",
    "        self.results = None\n",
    "        self.get_data() \n",
    "        \n",
    "    def get_data(self):\n",
    "        df = yf.download(self.symbol, start=self.start, end=self.end)\n",
    "        df = df.rename(columns={self.symbol: 'Close'})\n",
    "        data = df.Close\n",
    "        data[\"returns\"] = np.log(data.Close.div(data.Close.shift(1)))\n",
    "        data[\"SMA_S\"] = data.Close.rolling(self.SMA_S).mean()\n",
    "        data[\"SMA_L\"] = data.Close.rolling(self.SMA_L).mean()\n",
    "        data.dropna(inplace=True)\n",
    "        self.data2 = data\n",
    "        \n",
    "        return data\n",
    "    \n",
    "    def test_results(self):\n",
    "        data = self.data2.copy().dropna()\n",
    "        data[\"position\"] = np.where(data[\"SMA_S\"]>data[\"SMA_L\"],1,-1)\n",
    "        data[\"strategy\"] = data[\"returns\"]*data.position.shift(1)\n",
    "        data.dropna(inplace=True)   \n",
    "        data[\"returnsbh\"] = data[\"returns\"].cumsum().apply(np.exp)\n",
    "        data[\"returnsstrategy\"] = data[\"strategy\"].cumsum().apply(np.exp)        \n",
    "        perf = data[\"returnsstrategy\"].iloc[-1]\n",
    "        outperf = perf - data[\"returnsbh\"].iloc[-1]\n",
    "        self.results = data\n",
    "        \n",
    "        ret = np.exp(data[\"strategy\"].sum())\n",
    "        std = data[\"strategy\"].std()*np.sqrt(252)\n",
    "        \n",
    "        #return ret, std\n",
    "        return round(perf,6), round(outperf,6)\n",
    "    \n",
    "    def plot_results(self):\n",
    "        if self.results is None: \n",
    "            print(\"run the test please\")\n",
    "        else:\n",
    "            title= \"{}| SMA_S={} | SMA_L{}\".format(self.symbol, self.SMA_S, self.SMA_L)\n",
    "            self.results[[\"returnsbh\",\"returnsstrategy\"]].plot(title=title, figsize = (12,8))"
   ]
  }
 ],
 "metadata": {
  "hide_input": false,
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
