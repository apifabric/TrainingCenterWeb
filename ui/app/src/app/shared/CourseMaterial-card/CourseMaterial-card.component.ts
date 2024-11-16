import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CourseMaterial-card.component.html',
  styleUrls: ['./CourseMaterial-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CourseMaterial-card]': 'true'
  }
})

export class CourseMaterialCardComponent {


}