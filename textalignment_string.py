{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf110
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Avenir-Book;\f2\fnil\fcharset0 Menlo-Regular;
}
{\colortbl;\red255\green255\blue255;\red43\green50\blue61;\red43\green50\blue61;\red255\green255\blue255;
\red53\green59\blue76;\red246\green246\blue246;\red53\green59\blue76;\red241\green249\blue255;\red53\green59\blue71;
\red241\green249\blue255;\red53\green59\blue71;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh14980\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs32 \cf0 # 
\f1 \cf2 \expnd0\expndtw0\kerning0
 \cf3 \cb4 \outl0\strokewidth0 \strokec3 to replace the blank (
\f2 \cf5 \cb6 \strokec5 ______
\f1 \cf3 \cb4 \strokec3 ) with 
\i rjust, ljust
\i0  or 
\i center
\i0 .
\f0 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
#  string alignment\
\
#Replace all ______ with rjust, ljust or center. \
\
thickness = int(raw_input()) #This must be an odd number\
c = 'H'\
\
#Top Cone\
for i in range(thickness):\
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)\
\
#Top Pillars\
for i in range(thickness+1):\
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)\
\
#Middle Belt\
for i in range((thickness+1)/2):\
    print (c*thickness*5).center(thickness*6)    \
\
#Bottom Pillars\
for i in range(thickness+1):\
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    \
\
#Bottom Cone\
for i in range(thickness):\
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)    \
\pard\pardeftab720\sl360\partightenfactor0

\f2\fs28 \cf7 \cb8 \expnd0\expndtw0\kerning0
\
# ABCDCDC\
# CDC\cf9 \

\f1\fs32 \cf2 \cb1 \
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0 \cf0 \kerning1\expnd0\expndtw0 \
\pard\pardeftab720\sl440\partightenfactor0

\f1 \cf2 \expnd0\expndtw0\kerning0
# Output\
\pard\pardeftab720\sl360\partightenfactor0

\f2\fs28 \cf7 \cb8 #     \cf5 \cb10 \outl0\strokewidth0 \strokec5 H    \
\pard\pardeftab720\sl360\partightenfactor0
\cf5 #    HHH   \
#   HHHHH  \
#  HHHHHHH \
# HHHHHHHHH\
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHHHHHHHHHHHHHHHHHHHHHH   \
#   HHHHHHHHHHHHHHHHHHHHHHHHH   \
#   HHHHHHHHHHHHHHHHHHHHHHHHH   \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
#   HHHHH               HHHHH             \
                    HHHHHHHHH \
                     HHHHHHH  \
                      HHHHH   \
                       HHH    \
                        H \cf11 \strokec11 \
\pard\pardeftab720\sl360\partightenfactor0

\f1\fs32 \cf2 \cb1 \outl0\strokewidth0 \
\
}