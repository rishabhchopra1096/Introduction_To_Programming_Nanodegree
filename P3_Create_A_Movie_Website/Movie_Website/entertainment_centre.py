import media
import fresh_tomatoes

# Creating instances of my movie class with a list of my favorite movies.
toy_story=media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", #noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)


avatar=media.Movie("Avatar","A marine on an alien planet",
                    "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSfQy2_p_Q5LykieXxQZ7B0Eqh9c2EpdUgvHN3xc0ncl02Q9_ZVnA",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(avatar.storyline)
# avatar.show_trailer()


hp7_ii=media.Movie("Harry Potter and The Dealthly Hallows Part II",
                    "The last chapter of the world wide phenomenon. "\
                    "It all ends here.",
                    "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg", #noqa
                    "https://www.youtube.com/watch?v=mObK5XD8udk")
# hp7_ii.show_trailer()

the_social_network=media.Movie("The Social Network",
                    "You do not make 500 million friends without making a few enemies.",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6SB-NhwAbKwwb-f34EirKmkIhO0GAbEyDsQt1vcsXfdPn-P0Xtg", #noqa
                    "https://www.youtube.com/watch?v=lB95KLmpLR4")

the_great_gatsby=media.Movie("The Great Gatsby",
                    "Based on F. Scott Fitzgerald's novel capturing a cross "\
                    "section of American Society.",
                    "http://i.ebayimg.com/images/i/262109664882-0-1/s-l1000.jpg", #noqa
                    "https://www.youtube.com/watch?v=sN183rJltNM")

intersteller=media.Movie("Intersteller",
                    "In the future, Earth is slowly becoming uninhabitable. "\
                    "Ex-NASA pilot Cooper, along with a team of researchers, "\
                    "is sent on a planet exploration mission to report which "\
                    "planet can sustain life",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB", #noqa
                    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

# Putting the movies in a list to pass on to the script that creates our page.
movies=[toy_story,avatar,hp7_ii,the_social_network,the_great_gatsby,intersteller]

def main():
    """Creates the movies web page."""
    fresh_tomatoes.open_movies_page(movies)

main()
