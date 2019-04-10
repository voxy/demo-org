# Docker installation

**Clone the repository:**

`git clone http://github.com/voxy/demo-org`
`cd demo-org`

**Build the container image:**

`docker build -t voxy/demo-org:latest .

**Run the container:**

`docker run -p 8005:8005 -it voxy/demo-org:latest`

**Access the site in your browser:**

`http://localhost:8005`

**Done**

