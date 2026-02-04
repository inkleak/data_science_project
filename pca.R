# Clustering model for football

library(mclust)

PLdata<- read.csv("premier-player-23-24.csv",header = TRUE)

# sub-setting data by position

FW <- PLdata[ which(PLdata$Pos=='FW'),]
MF <- PLdata[ which(PLdata$Pos=='MF'),]
DF <- PLdata[ which(PLdata$Pos=='DF'),]
GK <- PLdata[ which(PLdata$Pos=='GK'),]



## Clustering

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

# Clustering by FW position

kmeansfitFW <- kmeans(ScaledFW,3)
clusterdata<- data.frame(ScaledFW, kmeansfitFW$cluster)
summary(clusterdata)

pca <- prcomp(ScaledFW)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfitFW$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
legend(-5,10,legend = c("Group 1","Group 2", "Group 3"),
       col = c(1,2,3), pch = 19)

# Clustering by DF

kmeansfitDF <- kmeans(ScaledDF,3)
clusterdata<- data.frame(ScaledDF, kmeansfitDF$cluster)
summary(clusterdata)

pca <- prcomp(ScaledDF)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfitDF$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
legend(-10,25,legend = c("Group 1","Group 2", "Group 3"),
       col = c(1,2,3), pch = 19)

# Clustering by MF

kmeansfitMF <- kmeans(ScaledMF,3)
clusterdata<- data.frame(ScaledMF, kmeansfitMF$cluster)
summary(clusterdata)

pca <- prcomp(ScaledMF)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfitMF$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
legend(-8,10,legend = c("Group 1","Group 2", "Group 3"),
       col = c(1,2,3), pch = 19)

# Clustering by GK

kmeansfitGK <- kmeans(ScaledGK,3)
clusterdata<- data.frame(ScaledGK, kmeansfitGK$cluster)
summary(clusterdata)

pca <- prcomp(ScaledGK)

summary(pca)
plot(pca)

plot(
  pca$x[,1], pca$x[,2],
  col = kmeansfitGK$cluster,
  pch = 19,
  xlab = "PC1",
  ylab = "PC2",
  main = "K-means Clusters (PCA)"
)
legend(-8,10,legend = c("Group 1","Group 2", "Group 3"),
       col = c(1,2,3), pch = 19)

# As for the goalkeeper stats we clearly do not have a large enough dataset
# for clustering to be viable

# attaching Cluster Membership to original Data sets


FW$clusters<-kmeansfitFW$cluster
DF$clusters<-kmeansfitDF$cluster
GK$clusters<-kmeansfitGK$cluster
MF$clusters<-kmeansfitMF$cluster


# Gaussian mixed model

GMM<- Mclust(ScaledFW,3)
GMMclusters <- predict(GMM)$classification

plot(ScaledFW, col = GMMclusters, main = "GMM Clustering")
points(GMM$parameters$mean, col = 1:3, pch = 8, cex = 2)
