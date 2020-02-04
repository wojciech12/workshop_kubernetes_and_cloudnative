## Best Practices

1. Minimal images

   - [ubuntu](https://hub.docker.com/_/ubuntu/)
   - [alpine](https://hub.docker.com/_/alpine)

   Caveat: take the OS you know.

   See: [baseimage](https://phusion.github.io/baseimage-docker/)

2. Do not use random docker images.

4. Use a specific tag for your base docker image.

5. Reduce the number of layers.

   What is the difference?

   <pre><code>RUN apt-get -y update && \
       apt-get install -y python
   </code></pre>

   vs

   <pre><code>RUN apt-get -y update
      RUN apt-get install -y python
   </code></pre>

   Notice: every <i>RUN</i>, <i>COPY</i>, <i>ADD</i> create a layer.

6. Reduce the size:

   - Be specific what you copy - <i>COPY</i>
   - Do not install, what you do not need, e.g., use <code>-no-install-recommends</code> for apt
   - Remove the cache:

    <pre><code>RUN apt-get -y update \
      && apt-get install -y \
      rm -rf /var/lib/apt/lists/*
    </code></pre>

7. Order! The things that changes the most should be the last to be added.

8. Use <code>.dockerignore</code>, see [example for the prometheus project](https://github.com/prometheus/golang-builder/blob/master/.dockerignore).

9. Development time: optimize the Docker to your work, do not be afraid to add as many layers as you need to speed up your development process.

10. Do you need to access a private git repositories inside Docker?

    <pre><code>docker build -t mojdocker . \
    -f Dockerfile \
    --build-arg GITHUB_TOKEN=TOKEN
    </code></pre>

    and multistage.

12. Multi-stage builds, see [example](multi-stage/).

13. Mountable secrets for building Docker Images (beta), see [example](secret-mount).

14. Do not use *latest*.

15. Try not to run your application as a <i>root</i> user.

16. Advance:

    - rebuild your base images / pull new ones
    - do not put secrets in your image, see the multi-stage and the mountable secrets.

## References

- https://github.com/goodwithtech/dockle
- https://github.com/hadolint/hadolint
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
