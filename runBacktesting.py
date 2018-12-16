# encoding: UTF-8
"""
展示如何执行策略回测。
"""
from __future__ import division
from ctaBacktestingctp import BacktestingEngine
from util.ctaBase import *

if __name__ == '__main__':
    from strategymulti import MultiStrategy
    # from strategytest import CLStrategy
    # 创建回测引擎
    engine = BacktestingEngine()

    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)
    # 设置使用的历史数据库
    engine.setDatabase('test_database')

    # 设置回测用的数据起始日期，initHours 默认值为 0
    engine.setStartDate('20160101 21:00')   
    engine.setEndDate('20180930 08:00')
    # 设置产品相关参数
    symbolList=['RB',
                'RU',
                'AG',
                'BU',
                'HC',
                'C',
                'J',
                'L',
                'M',
                'P',
                'V',
                'Y',
                'CS',
                'I',
                'JM',
                'PP',
                'CF',
                'TA',
                'FG',
                'MA',
                'RM',
                'ZC',
                'OI',
                'SR']
    Size={'J': 100.0,
        'JM': 60.0,
        'RB': 10.0,
        'RU': 10.0,
        'AG': 15.0,
        'BU': 10.0,
        'HC': 10.0,
        'C': 10.0,
        'L': 5.0,
        'M': 10.0,
        'P': 10.0,
        'V': 5.0,
        'Y': 10.0,
        'CS': 10.0,
        'I': 100.0,
        'PP': 5.0,
        'CF': 5.0,
        'TA': 5.0,
        'FG': 20.0,
        'MA': 10.0,
        'RM': 10.0,
        'ZC': 100.0,
        'OI': 10.0,
        'SR': 10.0,
        'CU': 5.0,
        'AU': 1000.0,
        'ZN': 5.0,
        'AL': 5.0,
        'NI': 10.0}
    PriceTick={'J': 0.5,
            'JM': 0.5,
            'RB': 1,
            'RU': 5,
            'AG': 1,
            'BU': 2,
            'HC': 1,
            'C': 1,
            'L': 5,
            'M': 1,
            'P': 2,
            'V': 5,
            'Y': 2,
            'CS': 1,
            'I': 0.5,
            'PP': 1,
            'CF': 5,
            'TA': 2,
            'FG': 1,
            'MA': 1,
            'RM': 1,
            'ZC': 0.2,
            'OI': 1,
            'SR': 1,
            'CU': 10,
            'AU': 0.05,
            'ZN': 5,
            'AL': 5,
            'NI': 1}
    engine.setSymbolList(symbolList)
    engine.setCapital(10000000)  # 设置起始资金，默认值是1,000,000
    engine.setSlippage(0)     # 股指1跳
    engine.setRate(0.3/10000)   # 万0.3
    engine.setSize({sym: Size[sym] for sym in symbolList})         # 股指合约大小 
    engine.setPriceTick({sym: PriceTick[sym] for sym in symbolList})    # 股指最小价格变动
    
    # 策略报告默认不输出，默认文件夹生成于当前文件夹下
    engine.setLog(True,"D:\\log\\")        # 设置是否输出日志和交割单, 默认值是不输出False
    engine.setCachePath("D:\\backtest_data\\") # 设置本地数据缓存的路径，默认存在用户文件夹内
    
    # 在引擎中创建策略对象
    d = {'symbolList':symbolList}
    engine.initStrategy(MultiStrategy,d)
    
    # 开始跑回测
    engine.runBacktesting()

    # 显示回测结果
    engine.showBacktestingResult()
    engine.showDailyResult()