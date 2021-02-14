import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-my-card',
  templateUrl: './my-card.component.html',
  styleUrls: ['./my-card.component.scss']
})
export class MyCardComponent implements OnInit {

  @Input() item: {title: string, body: string};
  
  constructor() { }

  ngOnInit(): void {
  }

}
