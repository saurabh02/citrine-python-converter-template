FROM citrine-executor-python:latest-onbuild

# Add commands here if you want
# Note that these have already been run via onbuild:
# ADD . /usr/local/ingest/compute
# RUN pip install -r requirements.txt
# RUN python ./setup.py install

# This is the standard entrypoint
# Don't change unless you know what you are doing
ENTRYPOINT ["ruby", "../wrap.rb"]
CMD ["--manifest_url=manifest.json"]
