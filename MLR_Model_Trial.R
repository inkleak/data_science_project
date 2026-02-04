#MLR model for football

PLdata<- read.csv("premier-player-23-24.csv",header = TRUE)

# sub-setting data by position

FW <- PLdata[ which(PLdata$Pos=='FW'),]
MF <- PLdata[ which(PLdata$Pos=='MF'),]
DF <- PLdata[ which(PLdata$Pos=='DF'),]
GK <- PLdata[ which(PLdata$Pos=='GK'),]

# Prepping data, sub-setting by position

PLdata_num <- PLdata[, sapply(PLdata, is.numeric)]
ScaledData<- scale(PLdata_num)

ScaledFW <- as.data.frame(scale(FW[, sapply(FW, is.numeric)]))
ScaledMF <- as.data.frame(scale(MF[, sapply(MF, is.numeric)]))
ScaledDF <- as.data.frame(scale(DF[, sapply(DF, is.numeric)]))
ScaledGK <- as.data.frame(scale(GK[, sapply(GK, is.numeric)]))

# Removing columns with all zeroes/nan values

ScaledDF<- ScaledDF[ , colSums(is.na(ScaledDF)) == 0 ]
ScaledGK<- ScaledGK[ , colSums(is.na(ScaledGK)) == 0 ]

lmFW <- lm(PLdata_num$Gls~PLdata_num$Age+PLdata_num$X90s+PLdata_num$Ast+PLdata_num$xG)
summary(lmFW)
plot(lmFW)



#polynomial regression

x<- poly(PLdata_num$Age,degree = 3, raw = FALSE)
y<- poly(PLdata_num$X90s,degree = 3, raw = FALSE)
z<- poly(PLdata_num$Ast_90,degree = 3, raw = FALSE)
w<- poly(PLdata_num$xG_90, degree = 3, raw = FALSE)

pmFW <- lm(PLdata_num$Gls~x+y+z+w)
summary(pmFW)

