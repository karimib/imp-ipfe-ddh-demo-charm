# IMP-IPFE-DDH

## Scheme

The following project implements the Inner Product Functional Encryption Scheme under the DDH Assumption as described on p.7/8 of the following paper

* [Simple Functional Encryption Schemes for Inner Products](https://eprint.iacr.org/2015/017)

## Structure

* [ipfeddh.py](./qfebounded.py) contains the implementation of the scheme
* [ipfehelpers.py](./qfehelpers.py) helper functions used by the scheme
* [benchmark.py](./benchmark.py) calls the scheme in different ways and provides benchmarks

## Prerequisites

* Docker or Podman (if using podman replace the "docker" with "podman" in the instructions below)

## Usage

Clone the repository

```shell
git clone https://github.com/karimib/imp-ipfe-ddh-demo-charm.git
cd imp-ipfe-ddh-demo-charm
```

Build the image (assuming your in the root directory)

```shell
docker build -t ipfeddhdemo:v1 .
```

Create a container from the image

```shell
docker run ipfeddhdemo:v1 
```

Mount a volume to save benchmark csv

````shell
docker run -v "${PWD}/results:/data" ipfeddhdemo:v1 
````
