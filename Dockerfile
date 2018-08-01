FROM python:3.7.0

ENV PROJECT_DIR /code
ENV APP_USER user_administration
ENV DJANGO_SETTINGS_MODULE="user_administration.settings.base"

# Default options to production
ARG PIPENV_OPTIONS="--system --ignore-pipfile --deploy"

# Copy project
COPY . ${PROJECT_DIR}

# Set working dir
WORKDIR ${PROJECT_DIR}

# Copy and install requirements
RUN pip3 install pipenv
RUN pipenv install $PIPENV_OPTIONS

# Securing
RUN groupadd -g 1000 -r ${APP_USER} \
    && useradd -u 1000 -r -m \
    -g ${APP_USER} ${APP_USER} \
    -s /usr/sbin/nologin \
    --home-dir ${PROJECT_DIR}

RUN chown -R ${APP_USER}:${APP_USER} ${PROJECT_DIR}

USER ${APP_USER}
