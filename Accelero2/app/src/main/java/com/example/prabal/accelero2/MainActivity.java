package com.example.prabal.accelero2;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.app.Activity;
import android.os.SystemClock;
import android.support.annotation.IntegerRes;
import android.text.Html;
import android.view.Menu;
import android.widget.TextView;
import prabal.accelero2.R;

import java.text.DecimalFormat;






public class MainActivity extends Activity implements SensorEventListener {

    private SensorManager sensorManager;

    TextView x;
    TextView y;
    TextView z;
    TextView w;

    String sx, sy, sz, sw;
    double xxval, yyval, zzval;

    long delay = 200000;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        x = (TextView) findViewById (R.id.textView2);
        y = (TextView) findViewById (R.id.textView3);
        z = (TextView) findViewById (R.id.textView4);
        w = (TextView) findViewById(R.id.textView5);


        sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);

        sensorManager.registerListener(this, sensorManager.getDefaultSensor
                (Sensor.TYPE_ACCELEROMETER), SensorManager.SENSOR_DELAY_UI );
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        //getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }

    @Override
    public void onAccuracyChanged(Sensor arg0, int arg1) {
        // TODO Auto-generated method stub

    }

    int num = 0;
    final double alpha = 0.8;

    @Override
    public void onSensorChanged(SensorEvent event) {

       // SystemClock.sleep(100);
        // TODO Auto-generated method stub

        if(event.sensor.getType() == Sensor.TYPE_ACCELEROMETER){

            double xVal = event.values[0];
            double yVal = event.values[1];
            double zVal = event.values[2];
            double[] gravity = new double [] {0,1,2};





            // Isolate the force of gravity with the low-pass filter.
            gravity[0] = alpha * gravity[0] + (1 - alpha) * event.values[0];
            gravity[1] = alpha * gravity[1] + (1 - alpha) * event.values[1];
            gravity[2] = alpha * gravity[2] + (1 - alpha) * event.values[2];

            xVal = event.values[0] - gravity[0];
            yVal = event.values[1] - gravity[1];
            zVal = event.values[2] - gravity[2];

            xxval = rountToDouble(xVal);
            yyval = rountToDouble(yVal);
            zzval = rountToDouble(zVal);




            //sx = "X Value : <font color = '#800080'> " + Integer.parseInt(String.valueOf(xVal)) + "</font>";
            sx = "X Value : <font color = '#800080'> " + xxval + "</font>";
            sy = "Y Value : <font color = '#800080'> " + yyval + "</font>";
            sz = "Z Value : <font color = '#800080'> " + zzval + "</font>";
            sw = "Count " + num ;




            num++;


            x.setText(Html.fromHtml(sx));
            y.setText(Html.fromHtml(sy));
            z.setText(Html.fromHtml(sz));
            w.setText(Html.fromHtml(sw));



        }
    }

    @Override
    protected void onResume() {
        super.onResume();
       
    }

    double rountToDouble(double num)
    {
        DecimalFormat tdf = new DecimalFormat("#.###");
        return Double.valueOf(tdf.format(num));


    }
}


