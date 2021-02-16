# Spaghetti Bin

## Intro
	
	It's a simple Blog-post pastebin-like web project.

## Logic?

	The landing/index page displays a stack of posts, sorted in descending order by updated_at property (fresh on top, older - lower).

	2 buttons on top: CREATE (a new post) and REFRESH (fetch available posts).
	2 buttons for each post div: 
	*(when in read mode) EDIT and DELETE
	*(when in edit/create mode) SAVE and CANCEL

	All actions are handled through requests implemented in JS.
	JS functions use fetch to perform requests to the API and then rebuild html body accordingly.
	All created posts are stored in sqlite DB.

*Please get in touch, if anything remains unclear.*