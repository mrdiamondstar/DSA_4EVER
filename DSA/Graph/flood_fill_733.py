from logging import addLevelName


class Solution:
    def floodfill(self,image , sr , sc , colour):
        rows=len(image)
        cols=len(image[0])
        
        original_colour=image[sr][sc]
        
        if original_colour==colour:
            return image
        
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        
        def dfs(rw , cl):
            
            image[rw][cl]==original_colour
            
            for dr , dc in directions:
                new_rw=rw+dr
                new_col=cl+dc
                
                if( 0 <= new_rw <= rows and
                  0 <=new_col<=cols and 
                  image[new_rw][new_col]==original_colour):
                     
                     dfs(new_rw , new_col)
                     
        dfs(sr,sc)
        return image
            
                
    