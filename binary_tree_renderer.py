from PIL import Image, ImageDraw
from math import pow


class PILTreeRenderer():

    def render_tree(self, tree):
        # Node consist of "data", "left", "right"
        # Tree traversing in depth with saving the longest node lengt
        n = self.get_depth(tree, 1) # Count of levels
        r = 20 # Radius of nodes
        d = r/1.5
        pic_width = r * (2 * int(pow(2, n)) - 1)
        pic_height = 2 * n * r
        image = Image.new("RGBA", (pic_width, pic_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        def draw_node(draw, node, level, x):
            y = r * (level) + r
            if node.left:
                xl = x - pic_width / pow(2, level + 2)
                draw.line((x-d, y-d, xl-d, (r*(level+2)+r)-d), width=1)
                draw_node(draw, node.left, level+2, xl)
            if node.right:
                xr = x + pic_width / pow(2, level + 2)
                draw.line((x-d, y-d, xr-d, (r*(level+2)+r)-d), width=1)
                draw_node(draw, node.right, level+2, xr)
            draw.ellipse((x-r, y-r, x, y), fill="blue", outline="red")
            draw.text((x-d, y-d), str(node.data))

        draw_node(draw, tree, 0, pic_width / pow(2, 1))

        del draw
        image.save("/home/igor/test.png", "PNG")

    def get_depth(self, node, depth):
        d_left = d_right = depth
        if node.left:
            d_left = self.get_depth(node.left, depth+1)
        if node.right:
            d_right = self.get_depth(node.right, depth+1)

        if d_left == d_right:
            return d_left
        elif d_left < d_right:
            return d_right
        elif d_right < d_left:
            return d_left