from pyecharts.charts import Bar,Pie
from pyecharts import options as opts

from streamlit_echarts import st_pyecharts

P = (
    Pie()
    .add(" 課程選修人數, 開課總數",[['[0,10)', 29], ['[10,30)', 53], ['[30,60)', 49], ['[60,]', 27]],        
         radius=["50%", "75%"],
         center=["35%", "50%"],
         rosetype="radius", 
        )
    .add(" 上午 課程",[['[0,10)', 12], ['[10,30)', 16], ['[30,60)', 15], ['[60,]', 8]],        
         radius=["25%", "38%"],
         center=["35%", "50%"],
        )
    .add(" 下午 課程",[['[0,10)', 17], ['[10,30)', 36], ['[30,60)', 34], ['[60,]', 19]],        
         radius=["10%", "18%"],
         center=["35%", "50%"],
        )
    .set_global_opts(title_opts=opts.TitleOpts(title="通識中心 112-1 課程", 
                                               subtitle='選課人數範圍',
                                               pos_left='left',
                                               pos_top='0%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="人數 {b}: {c} 門"))
)

weekday=['星期一','星期二','星期三','星期四','星期五']
B = (
    Bar()
    .add_xaxis(weekday)
    .add_yaxis(" 上午 課程數目", [7, 5, 13, 12, 7])
    .add_yaxis(" 下午 課程數目",[33, 26, 19, 18, 11] )
    .set_global_opts(title_opts=opts.TitleOpts(title="通識中心 112-1 課程", subtitle="每週課程 開課概況"))
)

st_pyecharts(P)
st_pyecharts(B)
