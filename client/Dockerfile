FROM node:12.18.1 as build-deps
WORKDIR /usr/src/app
COPY package.json yarn.lock ./
RUN yarn
COPY . ./
RUN yarn build

FROM nginx
COPY --from=build-deps /usr/src/app/dist /usr/share/nginx/html
ENV NGINX_PORT=8080
EXPOSE 8888
CMD ["sudo", "nginx", "-g", "daemon off;"]