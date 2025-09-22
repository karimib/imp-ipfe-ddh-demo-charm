# IMP-IPFE-DDH

## Scheme

The following project implements the Inner Product Functional Encryption Scheme under the DDH Assumption as described on p.7/8 of the following paper

* [Simple Functional Encryption Schemes for Inner Products](https://eprint.iacr.org/2015/017)

## Disclaimer:
Disclaimer
The code provided is for educational and research purposes only. It has not been reviewed, tested, or verified for security, reliability, or suitability in any environment. The code MUST NOT be used in production systems or for any purpose where failure, errors, or vulnerabilities could cause harm or damage.

The authors and contributors make no warranties or guarantees, express or implied, regarding the code, including but not limited to its correctness, safety, or fitness for any particular purpose. All use of this code is at your own risk. The authors explicitly disclaim any and all liability for direct, indirect, incidental, or consequential damages arising from the use, misuse, or inability to use the code.

## Structure

* [ipfeddh.py](./ipfeddh.py) contains the implementation of the scheme
* [ipfehelpers.py](./ipfehelpers.py) helper functions used by the scheme
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

## Benchmarking

The [benchmark.py](./benchmark.py) file contains two methods for benchmarking

| Method | Description |
| --- | --- |
| simulate_increasing_bits() | Compare the timings when increasing the security parameter (in bits) that instantiates the cyclic group G of prime order |
| simulate_increasing_length() | Compare the timings when increasing the length of the input vectors x and y|

to run them you have to uncomment line 108 and line 109 and build a new image as follows:

Build the image

```shell
docker build -t ipfeddhdemo:v1 .
```

Then mount a volume to save the benchmark csv to your disk:

````shell
docker run -v "${PWD}/results:/data" ipfeddhdemo:v1 
````
