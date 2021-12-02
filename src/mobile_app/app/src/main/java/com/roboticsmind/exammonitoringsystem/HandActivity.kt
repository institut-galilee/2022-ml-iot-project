package com.roboticsmind.exammonitoringsystem

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class HandActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_hand)
    }

    fun startSensorsService(view: android.view.View) {}
}