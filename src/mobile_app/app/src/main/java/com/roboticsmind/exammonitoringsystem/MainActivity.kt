package com.roboticsmind.exammonitoringsystem

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun startHandActivity(view: android.view.View) {
        val intent = Intent(this, HandActivity::class.java)
        startActivity(intent)
    }
    fun startHeadActivity(view: android.view.View) {
        val intent = Intent(this, HeadActivity::class.java)
        startActivity(intent)
    }
}