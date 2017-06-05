{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Avenir-Book;\f2\fnil\fcharset0 Menlo-Regular;
}
{\colortbl;\red255\green255\blue255;\red43\green50\blue61;\red255\green255\blue255;\red53\green59\blue76;
\red241\green249\blue255;\red53\green59\blue71;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs32 \cf0 # 
\f1 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2  Text wrap and fill()\
# task is to use fill()\

\f0 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
def wrap(string, max_width):\
    return textwrap.fill(string, max_width)\
\pard\pardeftab720\sl360\partightenfactor0

\f2\fs28 \cf4 \cb5 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 \
# ABCDEFGHIJKLIMNOQRSTUVWXYZ\
# 4\cf6 \strokec6 \

\f1\fs32 \cf2 \cb1 \strokec2 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0 \cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\pard\pardeftab720\sl440\partightenfactor0

\f1 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Output\
\pard\pardeftab720\sl360\partightenfactor0

\f2\fs28 \cf4 \cb5 \strokec4 # ABCD\
# EFGH\
# IJKL\
# IMNO\
# QRST\
# UVWX\
# YZ  \cf6 \strokec6 \

\f1\fs32 \cf2 \cb1 \strokec2 \
\
}