package com.roboticsmind.exammonitoringsystem

import com.roboticsmind.exammonitoringsystem.protobuf.lite.BlockingFilter
import com.roboticsmind.exammonitoringsystem.protobuf.lite.PredictionRequest
import com.roboticsmind.exammonitoringsystem.protobuf.lite.PredictionResponse
import com.roboticsmind.exammonitoringsystem.protobuf.lite.PredictorServiceGrpc
import io.grpc.Server
import io.grpc.netty.shaded.io.grpc.netty.NettyServerBuilder
import io.grpc.stub.StreamObserver

class RpcServer {
    companion object {
        const val PORT = 8089
    }

    class PredictorServiceImpl : PredictorServiceGrpc.PredictorServiceImplBase() {
        override fun predict(
            request: PredictionRequest?,
            responseObserver: StreamObserver<PredictionResponse>?
        ) {
            /*
            print("#############################")
            print("received a PredictionRequest!")
            print("#############################")
             */

            val response = PredictionResponse
                .newBuilder()
                .setFilter(
                    request?.url?.length?.let {
                        BlockingFilter
                            .newBuilder()
                            .setPointer(it.toLong()) // server logic: just for the test
                            .build()
                    })
                .build()
            responseObserver?.onNext(response)
            responseObserver?.onCompleted()

        }
    }

    private lateinit var server: Server

    fun setUp() {
        server = NettyServerBuilder // have to use Netty.. explicitly (instead of Managed..)
            .forPort(PORT)
            .addService(PredictorServiceImpl())
            .build()
        //server.start()
    }

    fun start() {
        server.start()
        println("Server started, listening on $PORT")
        Runtime.getRuntime().addShutdownHook(
            Thread {
                println("*** shutting down gRPC server since JVM is shutting down")
                //this@HelloWorldServer.stop()
                println("*** server shut down")
            }
        )
    }

    private fun stop() {
        server.shutdown()
    }

    fun blockUntilShutdown() {
        server.awaitTermination()
    }

}