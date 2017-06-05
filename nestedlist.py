{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Regular;\f2\fnil\fcharset0 Avenir-Book;
}
{\colortbl;\red255\green255\blue255;\red53\green59\blue76;\red241\green249\blue255;\red53\green59\blue71;
\red43\green50\blue61;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs32 \cf0 # nested list \
\
\
   \
students = sorted([[raw_input(), float(input())] for _ in range(int(input()))])\
secndLow = sorted(list(set(score for [_, score] in students)))[1]\
print ("\\n".join( name for [name, score] in students if score == secndLow))\
\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # 5\
# Harry\
# 37.21\
# Berry\
# 37.21\
# Tina\
# 37.2\
# Akriti\
# 41\
# Harsh\
# 39\cf4 \strokec4 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs32 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
\pard\pardeftab720\sl440\partightenfactor0

\f2 \cf5 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec5 # Output\
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs28 \cf2 \cb3 \strokec2 # Berry\
# Harry\cf4 \strokec4 \
\pard\pardeftab720\sl440\partightenfactor0

\f2\fs32 \cf5 \cb1 \strokec5 \
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs28 \cf4 \cb3 \strokec4 \
}