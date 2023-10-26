create table crypto_usd (
  id bigint generated by default as identity primary key,
  name text,
  symbol text,
  slug text,
  num_market_pairs integer,
  date_added timestamp,
  tags text,
  max_supply bigint,
  circulating_supply decimal,
  total_supply decimal,
  cmc_rank int,
  self_reported_circulating_supply decimal,
  tvl_ratio decimal,
  last_updated timestamp not null,
  quote_usd_price decimal,
  quote_usd_volume_24h decimal,
  quote_usd_volume_change_24h decimal,
  quote_usd_percent_change_1h decimal,
  quote_usd_percent_change_24h decimal,
  quote_usd_percent_change_7d decimal,
  quote_usd_percent_change_30d decimal,
  quote_usd_percent_change_60d decimal,
  quote_usd_percent_change_90d decimal,
  quote_usd_market_cap decimal,
  quote_usd_market_cap_dominance decimal,
  quote_usd_fully_diluted_market_cap decimal,
  quote_usd_tvl decimal,
  quote_usd_last_updated timestamp
  inserted_at timestamp with time zone default timezone('utc'::text, now()) not null
);

create table crypto_eur (
  id bigint generated by default as identity primary key,
  name text,
  symbol text,
  slug text,
  num_market_pairs integer,
  date_added timestamp,
  tags text,
  max_supply bigint,
  circulating_supply decimal,
  total_supply decimal,
  cmc_rank int,
  self_reported_circulating_supply decimal,
  tvl_ratio decimal,
  last_updated timestamp not null,
  quote_eur_price decimal,
  quote_eur_volume_24h decimal,
  quote_eur_volume_change_24h decimal,
  quote_eur_percent_change_1h decimal,
  quote_eur_percent_change_24h decimal,
  quote_eur_percent_change_7d decimal,
  quote_eur_percent_change_30d decimal,
  quote_eur_percent_change_60d decimal,
  quote_eur_percent_change_90d decimal,
  quote_eur_market_cap decimal,
  quote_eur_market_cap_dominance decimal,
  quote_eur_fully_diluted_market_cap decimal,
  quote_eur_tvl decimal,
  quote_eur_last_updated timestamp
  inserted_at timestamp with time zone default timezone('utc'::text, now()) not null
);

create table cti_rss_feeds (
  id bigint generated by default as identity primary key,
  description text, 
  type text,
  url text
);

create table cti_rss_feeds (
  id bigint generated by default as identity primary key,
  description text, 
  type text,
  url text,
  last_updated timestamp
);

create table if not EXISTS market_rss_feeds (
	id bigint generated by default as identity primary key,
  description text, 
  type text,
  url text,
  last_updated timestamp
);
create table if not exists market_news (
  id bigint generated by default as identity primary key,
  market_rss_feed_id bigint,
  title text,
  article text,
  url text,
  published_date timestamp,
  constraint fk_market_feed foreign key(market_rss_feed_id) REFERENCES market_rss_feeds(id)
);

create table if not exists cti_news (
  id bigint generated by default as identity primary key,
  cti_rss_feed_id bigint,
  title text,
  article text,
  url text,
  published_date timestamp,
  constraint fk_cti_feed foreign key(cti_rss_feed_id) REFERENCES cti_rss_feeds(id)
);

CREATE TABLE IF NOT EXISTS public.twitter_category
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying COLLATE pg_catalog."default" DEFAULT '50'::character varying,
    CONSTRAINT twitter_category_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.twitter_handle
(
    twitter_id character varying COLLATE pg_catalog."default" DEFAULT ''::character varying,
    twitter_handle character varying COLLATE pg_catalog."default" DEFAULT ''::character varying,
    name character varying COLLATE pg_catalog."default" DEFAULT ''::character varying,
    is_active boolean DEFAULT false,
    created_at timestamp with time zone DEFAULT now(),
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    twitter_avatar character varying COLLATE pg_catalog."default",
    CONSTRAINT twitter_handle_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.twitter_category_handles
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    handle_id uuid,
    category_id bigint,
    created_at timestamp with time zone DEFAULT now(),
    CONSTRAINT twitter_handle_categories_pkey PRIMARY KEY (id),
    CONSTRAINT twitter_category_handles_category_id_fkey FOREIGN KEY (category_id)
        REFERENCES public.twitter_category (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT twitter_category_handles_handle_id_fkey FOREIGN KEY (handle_id)
        REFERENCES public.twitter_handle (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.twitter_tweet
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    tweet_id character varying COLLATE pg_catalog."default" NOT NULL,
    tweet_text character varying COLLATE pg_catalog."default",
    tweet_created_at character varying COLLATE pg_catalog."default",
    is_active boolean,
    created_at timestamp with time zone DEFAULT now(),
    user_twitter_id character varying COLLATE pg_catalog."default",
    handle_id uuid,
    CONSTRAINT twitter_tweet_pkey PRIMARY KEY (id),
    CONSTRAINT twitter_tweet_tweet_id_key UNIQUE (tweet_id),
    CONSTRAINT twitter_tweet_handle_id_fkey FOREIGN KEY (handle_id)
        REFERENCES public.twitter_handle (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS public.twitter_scheduler_logs
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    last_run_date timestamp without time zone,
    tweet_count_total smallint,
    status character varying COLLATE pg_catalog."default",
    created_at timestamp with time zone DEFAULT now(),
    modified_at timestamp without time zone,
    CONSTRAINT twitter_scheduler_logs_pkey PRIMARY KEY (id)
);

