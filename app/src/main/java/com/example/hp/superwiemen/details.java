package com.example.hp.superwiemen;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

public class details extends Activity {
    private Button upload;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.details);

        upload = findViewById(R.id.upload);
        final String name = MainActivity.returnName();

        final EditText homeAdd  = (EditText) findViewById(R.id.home);


        final EditText workAdd  = (EditText) findViewById(R.id.work);

        upload.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String  home = homeAdd.getText().toString();
                System.out.println("home is "+ home);

                String  work = workAdd.getText().toString();
                System.out.println("work is "+ work);
                MainActivity.mDatabaseRef.child(name).child("home").setValue(home);
                MainActivity.mDatabaseRef.child(name).child("work").setValue(work);



            }

        });



    }

}
