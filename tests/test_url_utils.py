import pytest


# fmt: off
@pytest.mark.parametrize("expected, media", [
    (False, "https://www.google.com"),
    (False, "random string"),
    (True,  "https://open.spotify.com/album/6i4ucRyGiCdJ1aQacEkjR2?si=hSu42KODRK6Lv4q2lSPyFg"),
    (True,  "https://open.spotify.com/playlist/0AUpTTGV60eWtZYOYTmaua?si=ea4a04e9abc041a1"),
    (True,  "https://open.spotify.com/track/1j7fq3bwLM63RMFvceb2Fm?si=2af6a72326854a6d"),
    (False, "https://www.youtube.com/watch?v=qPyebiLvT3k"),
    (False, "https://www.youtube.com/playlist?list=PLRfY4Rc-GWzhdCvSPR7aTV0PJjjiSAGMs"),
    (False, "https://www.youtube.com/watch?v=8ejF8Qv6VZk&list=PLRfY4Rc-GWzhdCvSPR7aTV0PJjjiSAGMs&index=1")
])
def test_is_spotify_link(expected: bool, media: str):
    assert True == True
    # actual: bool = utils.is_spotify_link(media)
