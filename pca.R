# MLR model for football

PLdata<- read.csv("premier-player-23-24.csv",header = TRUE)

# sub-setting data by position

FW <- PLdata[ which(PLdata$Pos=='FW'),]
MF <- PLdata[ which(PLdata$Pos=='MF'),]
DF <- PLdata[ which(PLdata$Pos=='DF'),]
GK <- PLdata[ which(PLdata$Pos=='GK'),]



# Clustering

PLdata_num <- PLdata[, sapply(PLdata, is.numeric)]
ScaledData<- scale(PLdata_num)

ScaledFW <- scale(FW[, sapply(FW, is.numeric)])
ScaledMF <- scale(MF[, sapply(MF, is.numeric)])
ScaledDF <- scale(DF[, sapply(DF, is.numeric)])
ScaledGK <- scale(GK[, sapply(GK, is.numeric)])

kmeansfit <- kmeans(ScaledData,4)
aggregate(ScaledData,by=list(fit$cluster),FUN=mean)
clusterdata<- data.frame(ScaledData, fit$cluster)
summary(clusterdata)

pca <- prcomp(ScaledData)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfit$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
