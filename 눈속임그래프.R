library(extrafont)
candidates<- c("강기윤", "이재환", "여영국", "손석형", "진순정", "김종서", "없음", "모름/무응답") 
rates <- c(28.5, 5.3, 41.3, 4.6, 0.6, 0.9, 4.2, 14.5)
colour_candidates <- c("#DF0101", "#01DFD7", "#F7D358", "#FF8000", "#FA5858", "#585858", "#BDBDBD", "#BDBDBD")
barplot(rates)
c_rates <- format(rates, nsmall = 1, justify = "right")
a <- sapply(strsplit(c_rates, "[.]"), `[`, 1)
b <- sapply(strsplit(c_rates, "[.]"), `[`, 2)
b_perc <- paste(".", b, "%", sep = "")
par(family = "Malgun Gothic")
b1 <- barplot(rates, 
              axes = FALSE, 
              col = colour_candidates, 
              names.arg = NULL,
              cex.names = 1.2,
              ylim = c(0, max(rates) * 1.1))
mtext(side = 1, at = b1, line = 2, text = candidates, cex = 1.5)
text(x = b1, y = rates + rep(1.5, 8), 
     labels = paste(c_rates, "%", sep = ""), 
     col = colour_candidates
)
main_title <- "4월3일 보궐선거 창원 성산구 후보별 지지율(%)"
title(main = main_title, 
      cex.main = 1.6)
box(which = "figure", lwd = 4)
par(family = "Malgun Gothic")
b1 <- barplot(rates, 
              axes = FALSE, 
              col = colour_candidates, 
              names.arg = NULL,
              cex.names = 1.1,
              ylim = c(0, max(rates) * 1.1))
mtext(side = 1, at = b1, line = 0, text = candidates)
text(x = b1 - c(rep(0.2, 3), rep(0.2, 5)), y = rates + rep(1.6, 8), 
     labels = a, 
     col = colour_candidates, 
     cex = 1.1)
text(x = b1 + 0.2, y = rates + rep(1.6, 8), 
     labels = b_perc, 
     col = colour_candidates, 
     cex = 1.1)
main_title <- "4월3일 보궐선거 창원 성산구 후보별 지지율(%)"
note_text <- "질문내용-선생님께서는 이들 중에서 어떤 후보에게 투표하실 생각이십니까?"
title(main = main_title, 
      cex.main = 1.6)
text(x = mean(b1) - 3, y = max(rates) - -7, labels = note_text, cex = 0.8, adj = 0)
box(which = "outer", lwd = 3)
par(family = "Malgun Gothic")
b1 <- barplot(rates, 
              axes = FALSE, 
              col = colour_candidates, 
              names.arg = NULL,
              cex.names = 1.1,
              ylim = c(0, max(rates) * 1.2))
mtext(side = 1, at = b1, line = 0, text = candidates)
text(x = b1 - c(rep(0.2, 3), rep(0.2, 5)), y = rates + rep(1.6, 8), 
     labels = a, 
     col = colour_candidates, 
     cex = 1.1)
text(x = b1 + 0.2, y = rates + rep(1.6, 8), 
     labels = b_perc, 
     col = colour_candidates, 
     cex = 1.1)
main_title <- "4월3일 보궐선거 창원 성산구 후보별 지지율(%)"
title(main = main_title, 
      cex.main = 1.6)
text(x = mean(b1) - 4, y = max(rates) - -7, labels = note_text, cex = 0.9, adj = 0)
box(which = "outer", lwd = 3)
sub_title <-"- 조사기관: 창원시 생산구매 거주하는 만 19세 이상 남녀 200명
 - 조사방법: 무선전화면접 82.6%,유선전화연결 17.4%
 - 조사일시: 2019년 3월 25일 ~ 2019년 3월 26일(2일간)"
title(sub = sub_title,
      cex.main = 0.2)