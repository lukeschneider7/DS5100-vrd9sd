library(tidyverse)

# Scatterplot with cylinders different colors
mtcars %>%
  ggplot(
    mapping = aes(
      x = disp, 
      y = mpg)
  ) + 
  geom_point(size=3, aes(color=cyl)
  )

# Layers created by geom_ and stat_ functions
mtcars %>%
  ggplot(aes(
    x = disp, 
    y = mpg)) + 
  geom_point(size=3, aes(color=cyl)) + 
  stat_smooth(method = lm)

# Faceting: visual equivalent of grouping by
mtcars %>%
  ggplot(aes(
    x = disp,
    y = mpg)) + 
  geom_point(size=3, aes(color=cyl)) +
  stat_smooth(method = lm) + 
  facet_wrap(facets = vars(cyl))
 


# Examples using diamonds data
view(diamonds)
gg <-  ggplot(diamonds, aes(x=carat, y=price)) 
gg + geom_point(aes(
  size=carat,
  shape=cut,
  color='steelblue',
  stroke=2))

# Add X and Y axis labels
gg1 <- gg + geom_point(aes(color=color))
gg2 <- gg1 + labs(title='Diamonds', x='Carat', y='price')
gg2

# Change color of all text with theme()
gg2 + theme(text=element_text(color='red'))


# Changing plot and axis title and text size
gg3 <- gg2 + 
  theme(plot.title=element_text(size=30), 
        axis.title.x=element_text(size=25),
        axis.title.y=element_text(size=25),
        axis.text.x=element_text(size=10),
        axis.text.y=element_text(size=10)
  )
gg3

# Changing title face, color, line height
gg3 + 
  labs(title = "Plot Title\nSecond Line of Plot Title") +
  theme(plot.title = element_text(
    face="italic", 
    color="gold", 
    lineheight=.8)
  )

# Manually set point colors
gg3 + scale_colour_manual(
  name='Color Legend', 
  values=c('D'='maroon', 
           'E'='cyan', 
           'F'='lavender', 
           'G'='salmon', 
           'H'='white', 
           'I'='gold', 
           'J'='firebrick'))

# Adjust axis limits
gg3 + 
  coord_cartesian(xlim=c(0,3), ylim=c(2000, 5000)) + 
  stat_smooth()  # zoom in

# Change X, Y axis labels
gg3 + scale_y_continuous(
  breaks=seq(0, 18000, 3000)) +
  scale_x_continuous(
    labels=c("zero","one", "two", "three", "four", "five" ))

# Flip X and Y axis
gg3 + coord_flip()
