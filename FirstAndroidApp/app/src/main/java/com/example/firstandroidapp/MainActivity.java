package com.example.firstandroidapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Layout;
import android.widget.GridLayout;
import android.widget.TextView;

import org.w3c.dom.Text;

import static android.view.Gravity.CENTER;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        GridLayout MainMenuList = new GridLayout(this);
        MainMenuList.setOrientation(GridLayout.HORIZONTAL);
        MainMenuList.setRowCount(2);
        MainMenuList.setColumnCount(2);

        GridLayout.LayoutParams MainMenuListParams = new GridLayout.LayoutParams();
        MainMenuListParams.setGravity(CENTER);
        MainMenuListParams.height = GridLayout.LayoutParams.WRAP_CONTENT;
        MainMenuListParams.width = GridLayout.LayoutParams.MATCH_PARENT;

        TextView txt = new TextView(this);
        txt.setText("asdasdasd");
        MainMenuList.addView(txt, MainMenuListParams);


        MainMenuList.setLayoutParams(MainMenuListParams);

    }
}
