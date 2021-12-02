package com.roboticsmind.exammonitoringsystem

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import java.net.BindException

class HeadActivity : AppCompatActivity() {
    private val TAG = "[HeadActivity]"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_head)

        // connect to the hotspot

        // setup rpc server and start listening for incoming remote procedure calls
        // TODO
        //  - handle for example when user goes back and then returns to this activity: an instance
        //    of the server is already running and will produce "java.net.BindException: Address already in use".
        //  - handle server shutdown
        //  - prevent user from going back to the previous activity
        //  - etc.
        try {
            var server = RpcServer()
            server.setUp()
            server.start()
        } catch (e: BindException) {
            Log.d(TAG, "An instance of the Netty server is already running")
        }
    }

    fun startCamera(view: android.view.View) {
        val intent = Intent(this, CameraActivity::class.java)
        startActivity(intent)
    }
}